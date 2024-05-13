#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Network Emulator

"""
__author__ = "bitset.jp"
__copyright__ = "bitset.jp"
__credits__ = ["taka miyamura"]
#__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "taka miyamura"
__email__ = "info@bitset.jp"
__status__ = "Production"

import signal 
import os
import os.path
import sys
import time
import subprocess
import time
from enum import Enum
import readline
import datetime
import logging
import queue
import threading
import datetime

from common import *
import filter
import utils
import capture
import config_file

#############################################################################
# const
LOG_FILE = '/tmp/bitset_netem.log'
JST = datetime.timezone(datetime.timedelta(hours=9), 'JST')
BIN_DIR = os.getenv('BIN_DIR')

#############################################################################
# global
is_run = True
exit_code = 0

app_path = None
bridge = None

app_name = None
mount_info = None
mount_path = None
prompt = None

#############################################################################
# USB Storage
def read_mount_path():
  '''
  USB Storage
  '''
  global mount_path, mount_info

  mount_path = None

  if os.path.isfile(mount_info):
    with open(mount_info, "r") as file:
      try:
        mount_path =  file.readline().replace("\n", "")
        logging.info(mount_path)
      except Exception as e:
        logging.exception(e)


#############################################################################
# signal handler
msgs = queue.Queue(16)
print_thread = None

def print_thread_function(name):
  '''
  SIGNALハンドラー用の画面出力

  '''
  global msgs

  while is_run:
    if not msgs.empty():
      msg = msgs.get()
      cmd = msg[0]
      text = msg[2:]
      if cmd == "n":
        print(f"\n{text}")
      elif cmd == "e":
        print_error(text)
      elif cmd == "c":
        result = subprocess.check_output(text.split()).decode('utf-8')
        print(result, end='', flush=True)
      else:
        pass
      if msgs.empty():
        print(prompt,end='', flush=True)

    else:
      time.sleep(0.1)  


def sig_usr1(signum,stack):
  global msgs
  update_title()

  if mount_path is not None:
    msgs.put("n:insert USB memory")
    msgs.put(f"c:df -h {mount_path}")


def sig_usr2(signum,stack):
  global msgs
  update_title()
  msgs.put("n:remove USB memory")


def sig_child(signum,stack):
  '''
  tcpdump の異常終了を監視する
  '''
  global msgs

  (p1, p2) = capture.pids()

  if 0 < p1 or 0 < p2:
    try:
      pid, _ = os.waitpid(-1, os.WNOHANG)
      if 0 < pid and (pid == p1 or pid == p2):
        index = 0 if pid == p1 else 1
        capture.notify_sigchld(index)
        if capture.is_capture_mode():
          msgs.put(f"e:capture stopped eth{index}")
        else:
          msgs.put(f"n:capture stopped eth{index}")
        
        update_title()
        os.system('tmux send-keys -t 0  C-m')
    except Exception as e:
      logging.exception(e)

 

def sig_default(signum,stack):
  pass

def sig_init():
  logging.debug("### sig_init() ###")

  signal.signal(signal.SIGUSR1, sig_usr1)
  signal.signal(signal.SIGUSR2, sig_usr2)
  signal.signal(signal.SIGCHLD, sig_child)
  signal.signal(signal.SIGINT,  sig_default)
  signal.signal(signal.SIGTSTP, sig_default)
  signal.signal(signal.SIGQUIT, sig_default)


#############################################################################
#
prev_title = None

def update_title():
  global prev_title

  read_mount_path()

  if mount_path is None:
    title = app_name
  else:
    (e0, e1) = capture.status()
    #print(f"{e0}:{e1}")
    if e0 is False and e1 is False:
      title = f'{app_name} USB'
    else:
      title = f'{app_name} cap:'
      if e0 is True:
        title += "eth0"
      if e1 is True:
        if e0 is True:
          title += ","
        title += "eth1"

  if prev_title != title:
    subprocess.call(f'tmux set-option -g status-left "{title}"', shell=True)
    prev_title = title



#############################################################################
#
def start_capture(index, sec):
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"
  
  rotate_seconds = 3600

  if sec is not None:
    try:
      rotate_seconds = int(sec)

      if rotate_seconds < 60 or 3600 < rotate_seconds:
        print_operation_error("invalid rotate_seconds range ( 60 - 3600)")
        return
    except Exception as e:
      #logging.exception(e)
      print_operation_error(f"invalid rotate_seconds value: {sec}")
      return

  if mount_path is not None:

    devs = []
    if index == 0 or index is None:
      devs.append("eth0")
    if index == 1 or index is None:
      devs.append("eth1")

    capture.start_capture(devs, mount_path, rotate_seconds )
  else:
    print_operation_error("not found usb memory. (need usb memory) ")

def stop_capture():
  capture.stop_capture()
  show_usb()

  os.system('tmux send-keys -t 0  C-c')


def load_config(args):
  if mount_path is None:
    print_error("no usb memory")
    return
  config = config_file.load(mount_path, args[0])  
  if config:
    print(config)
    filter.set_from_dict(config)
  else:
    print_error("failed to load config")

def save_config(args):
  if mount_path is None:
    print_error("no usb memory")
    return
  dict = filter.get_dict()
  if dict:
    dict['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    config_file.save(mount_path, args[0], dict)


def show_usb():
  if mount_path is not None:
    print("=== USB ===")
    result = subprocess.check_output(f"ls -g -o -h -t --time-style=iso {mount_path}".split()).decode('utf-8')
    print(result, end='\n')
    #print("")
    result = subprocess.check_output(f"df -h {mount_path}".split()).decode('utf-8')
    print(result, end='\n')
  else:
    print_operation_error("no usb memory")


def show_status():
  now = datetime.datetime.now(JST)
  print(f"--- {datetime.datetime.now(JST).strftime('%H:%M:%S')} ---")
  for i in range(2):
    (dev, setting, stat) = filter.get_status(i)

    print(f"[{i}] {dev}: \x1b[33m {setting}\x1b[0m")

    for i, line in enumerate(stat):
      print(f"  \x1b[36m{line}\x1b[0m")


def show_edit_buffer():
  for i in range(2):
    opt = filter.setting(i)
    print(f"[{i}] {opt.dev}: \x1b[36m {opt}\x1b[0m")


def get_prompt(index):
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  changed = filter.is_changed(index)
  prompt = "\x1b[1m\x1b[43m" if changed else ''
  
  prompt += "{}".format("a" if index is None else index)

  prompt += "*\x1b[0m" if changed else ' '

  prompt += "> "
  return prompt


def poweroff():
  os.system('sudo poweroff')

#############################################################################
# Command
def help(args):
  pane = 1
  cmd = args[0] if args is not None and len(args) != 0 else ''
  
  subprocess.call(f"tmux send-keys -t {pane} \"{BIN_DIR}/help.sh {cmd}\" C-m", shell=True)


def dstat():
  pane = 2
  subprocess.call(f"tmux send-keys -t {pane} C-c", shell=True)
  subprocess.call(f"tmux send-keys -t {pane}  \"dstat -t --net -N eth0,eth1\" C-m", shell=True)


def monitor(index):
  pane_base=3
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  for i in range(2):
    if index == i or index is None:
      pane = pane_base + i
      subprocess.call(f"tmux send-keys -t {pane}  C-c", shell=True)
      subprocess.call(f"tmux send-keys -t {pane}  \"LANG=C sudo -E iftop -i eth{i} -n\" C-m", shell=True)


def tcpdump(index):
  pane_base=3
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

  for i in range(2):
    if index == i or index is None:
      pane = pane_base + i
      subprocess.call(f"tmux send-keys -t {pane}  C-c", shell=True)
      subprocess.call(f"tmux send-keys -t {pane}  \"sudo tcpdump -q -i eth{i}\" C-m", shell=True)


def height(args):
  MIN = 10
  MAX = 35

  usage = f"height [{MIN} - {MAX}]"
  if args is None or len(args) == 0:
    print_usage(usage)
    return
  
  h = int(args[0])
  if h < MIN or MAX < h:
    print_usage(usage)
    return
  subprocess.call(f"tmux resize-pane -y {h} -t 3", shell=True)


def ifconfig(index):
  assert index == 0 or index == 1 or index is None, f"invalid index:{index}"
  for i in range(2):
    if index == i or index is None:
      try:
        result = subprocess.check_output(f"ifconfig eth{i}".split()).decode('utf-8')
        print(result, end='')
      except subprocess.CalledProcessError as e:
        logging.exception(e)


#############################################################################
#
def init():
  """ 初期化 """
  global app_path, bridge, app_name, mount_info, print_thread

  logging.debug("### init() ###")

  readline.set_history_length(1000)

  print_thread = threading.Thread(target=print_thread_function, args=("msg_print",))
  print_thread.start()


  sig_init()

  app_path = os.getenv('BASE_PATH')
  bridge = os.getenv('BRIDGE')

  filter.setup(["eth0", "eth1"])
  
  app_name = os.getenv('TITLE')
  mount_info = os.getenv('MOUNT_INFO')


def main():
  global is_run
  global exit_code
  global prompt
  logging.debug("### main() ###")

  index = None

  try:
    update_title()
    show_status()

    while is_run:
      assert index == 0 or index == 1 or index is None, f"invalid index:{index}"

      prompt = get_prompt(index)
      args = input(prompt).lower().split()
      
      if not args: #len(args) == 0:
        show_status()
        continue

      cmd = args[0]
      
      if  cmd == "0":
        index = 0
      elif cmd == "1":
        index = 1
      elif cmd == "a":
        index = None     
      elif cmd == "edit":
        show_edit_buffer()
      elif cmd == "update":
        filter.update(index)
        show_status()
      elif cmd == "reset":
        filter.reset(None if 1 < len(args) and args[1] == "all" else index)
        show_status()
      elif cmd == "help" or cmd == "h":
        help(args[1:])
      elif cmd == "stat":
        dstat()
      elif cmd == "mon" or cmd == "iftop":
        monitor(index)
      elif cmd == "packet" or cmd == "tcpdump":
        tcpdump(index)
      elif cmd == "ifconfig":
        ifconfig(index)
      elif cmd == "height":
        height(args[1:])
      elif cmd == "rtc":
        if utils.set_time(args[1:]):
          show_status()
      elif cmd == "keyboard":
        utils.set_keyboard(args[1:])
      elif cmd == "clear" or cmd == "cls":
        subprocess.run(["clear"])
        show_status()
      elif cmd == "usb" or  cmd == "ls":
        show_usb()
      elif cmd == "cap":
        sub = args[1] if 1 < len(args) else None
        if sub == "start":
          start_capture(index, args[2] if 2 < len(args) else None )
        elif sub == "stop":
          stop_capture()
        else:
          print("invalid option: cap {start|stop}")
      elif cmd == "limit":
        filter.set_opt_limit(index, args[1:])
      elif cmd == "delay":
        filter.set_opt_delay(index, args[1:])
      elif cmd == "loss":
        filter.set_opt_loss(index, args[1:])
      elif cmd == "duplicate" or cmd == "dup":
        filter.set_opt_duplicate(index, args[1:])
      elif cmd == "corrupt":
        filter.set_opt_corrupt(index, args[1:])
      elif cmd == "reorder":
        filter.set_opt_reorder(index, args[1:])
      elif cmd == "rate":
        filter.set_opt_rate(index, args[1:])
      elif cmd == "reload":
        exit_code = 1
        is_run = False
        break
      elif cmd == "load":
        load_config(args[1:])
      elif cmd == "save":  
        save_config(args[1:])
      elif cmd == "exit_xxx":
        exit_code = 99
        is_run = False
        break
      elif cmd == "poweroff":
        poweroff()
        break
      else:
        print_operation_error("invalid command")

      #os.system('tmux send-keys -t 0  C-c')
  except BaseException as e:
    logging.exception(e)

  if capture.is_running():
    capture.stop_capture()

if __name__ == '__main__':

  os.system('rm -f {0}'.format(LOG_FILE))
  logging.basicConfig(filename=LOG_FILE,
                      level=logging.DEBUG,
                      format="%(asctime)s.%(msecs)-3d [%(levelname)s] %(filename)s#%(funcName)s() @%(lineno)d: %(message)s",
                      datefmt='%H:%M:%S')
  logging.debug("### START ###")

  init()

  while is_run:
    main()

  filter.delete_all()
  print_thread.join(3)

  logging.debug("### END ###")
  sys.exit(exit_code)
