# -*- coding: utf-8 -*-

import subprocess
from subprocess import Popen
import logging
from setting import *
from common import *

'''
{
    "delay": "100ms 10ms 25%",
    "distribution": "normal",
    "reorder": "25% 50%",
    "loss": "0.3% 25%",
    "duplicate": "1%",
    "corrupt": "0.1%",
    "rate": "256kbit",
    "buffer": 1600,
    "limit": 3000,
    "dst": "10.10.10.0/24"
}
'''

'''
Usage: ... netem 
  [ limit PACKETS ]
  [ delay TIME [ JITTER [CORRELATION]]]
  [ distribution {uniform|normal|pareto|paretonormal} ]
  [ corrupt PERCENT [CORRELATION]]
  [ duplicate PERCENT [CORRELATION]]
  [ loss random PERCENT [CORRELATION]]
  [ loss state P13 [P31 [P32 [P23 P14]]]
  [ loss gemodel PERCENT [R [1-H [1-K]]]
  [ ecn ]
  [ reorder PERCENT [CORRELATION] [ gap DISTANCE ]]
  [ rate RATE [PACKETOVERHEAD] [CELLSIZE] [CELLOVERHEAD]]
  [ slot MIN_DELAY [MAX_DELAY] [packets MAX_PACKETS] [bytes MAX_BYTES]]
  [ slot distribution {uniform|normal|pareto|paretonormal|custom} DELAY JITTER [packets MAX_PACKETS] [bytes MAX_BYTES]]
'''


#############################################################################
#
settings = []

#############################################################################
# public
#############################################################################
def setting(index):
  global settings
  assert index == 0 or index == 1, f"invalid index:{index}"
  return settings[index]

# 初期設定
def setup(devs):
  global settings
  for dev in devs:
    settings.append(Setting(dev))

  for opt in settings:
    __init_filter(opt)


def is_changed(index):
  global settings
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  for i, opt in enumerate(settings):
    if (index == i or index is None) and opt.is_changed():
      return True
  return False

# ブリッジの有無の判定
def check_bridge(bridge):
  #ret = subprocess.call("brctl show {}".format(bridge))
  ret = subprocess.call(["brctl","show", bridge],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
  return True if ret == 0 else False


# フィルター削除
def delete_all():
  for opt in settings:
    ret = subprocess.call(f"sudo tc qdisc del dev {opt.dev} root".split())


# フィルター設定確認
def get_status(index):
  global settings
  assert index == 0 or index == 1, f"invalid index:{index}"
  try:
    dev = settings[index].dev
    setting = subprocess.check_output(f"tc qdisc show dev {dev}".split()).decode('utf-8').replace("\n", "")
    stat = subprocess.check_output(f"tc -s qdisc show dev {dev}".split()).decode('utf-8').splitlines()

    if stat[0] == setting:  # qdisc netem 8050: root refcnt 6 limit 1000
      stat = stat[1:]
    return (dev, setting, stat)
  except Exception as e:
    print(e)
    logging.exception(e)


# フィルタークリア
def reset(index):
  global settings
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  try:
    for i, opt in enumerate(settings):
      if index == i or index is None:
        __init_filter(opt)

  except Exception as e:
    print(e)
    logging.exception(e)


# フィルタ設定変更
def update(index):
  global settings
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  try:
    for i, opt in enumerate(settings):
      if index == i or index is None:
        (ret, msg) = opt.validate()

        if ret is True:
          (ret, msg) = __update_filter(opt)

        if ret is False:
          err = f"[{opt.dev}] {msg}"
          print_error(err)
          logging.error(err)

  except Exception as e:
    print(e)
    logging.exception(e)


##################################################################################
# Option
##################################################################################

# キャパシティ
def set_opt_limit(index, args):
  global settings
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  for i, opt in enumerate(settings):
    if index == i or index is None:
      opt.set_limit(args)



# 遅延オプション設定
def set_opt_delay(index, args):
  global settings
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  for i, opt in enumerate(settings):
    if index == i or index is None:
      opt.set_delay(args)


# ロスオプション設定
def set_opt_loss(index, args):
  global settings
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  for i, opt in enumerate(settings):
    if index == i or index is None:
      opt.set_loss(args)


# 重複オプション設定
def set_opt_duplicate(index, args):
  global settings
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  for i, opt in enumerate(settings):
    if index == i or index is None:
      opt.set_duplicate(args)


# パケット破壊オプション設定
def set_opt_corrupt(index, args):
  global settings
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  for i, opt in enumerate(settings):
    if index == i or index is None:
      opt.set_corrupt(args)


# 再送要求設定
def set_opt_reorder(index, args):
  global settings
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  for i, opt in enumerate(settings):
    if index == i or index is None:
      opt.set_reorder(args)

# 帯域制限
def set_opt_rate(index, args):
  global settings
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  for i, opt in enumerate(settings):
    if index == i or index is None:
      opt.set_rate(args)


##################################################################################
# private
##################################################################################
# フィルター作成
def __init_filter(opt):
  ret = subprocess.call(f"sudo tc qdisc del dev {opt.dev} root".split(), stderr=subprocess.DEVNULL)
  ret = subprocess.call(f"sudo tc qdisc add dev {opt.dev} root netem limit {opt.get_limit()}".split())
  opt.clear()


# フィルター設定
def __update_filter(opt):
  if opt.is_changed() is False:
    return

  params = ""

  if opt.delay is not None:
    tmp = f" delay {opt.delay[0]} "
    if 2 <= len(opt.delay):
      tmp += f" {opt.delay[1]} "
      if 3 <= len(opt.delay):
        tmp += f" {opt.delay[2]} "
    params += tmp

  if opt.loss is not None:
    tmp = f" loss {opt.loss[0]} "
    params += tmp

  if opt.duplicate is not None:
    tmp = f" duplicate {opt.duplicate[0]} "
    params += tmp

  if opt.corrupt is not None:
    tmp = f" corrupt {opt.corrupt[0]} "
    params += tmp

  if opt.reorder is not None:
    tmp = f" reorder {opt.reorder[0]} "
    params += tmp

  if opt.rate is not None:
    tmp = f" rate {opt.rate[0]} "
    params += tmp

  assert 0 < len(params) or opt.limit is not None
  
  cmd = f"sudo tc qdisc change dev {opt.dev} root netem limit {opt.get_limit()} {params}"
  print(f"execute: {cmd}")
  logging.debug(cmd)
  #ret = subprocess.call(cmd.split())
  ret = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE )

  if ret.returncode == 0:
    opt.clear()
    return (True, None)
  else:
    return (False, ret.stderr.decode('utf-8').replace("\n", " "))

