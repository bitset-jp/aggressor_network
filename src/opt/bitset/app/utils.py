#!/usr/bin/env python3

import datetime
import os
import subprocess
import logging

from common import *

def set_time(args):
  usage = "rtc  YYYY-MM-DD hh:mm:ss"

  if args is None or len(args) != 2:
    print_usage(usage)
    return False

  try:
    str = f"{args[0]} {args[1]}"

    timestamp = datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S')

    os.system(f'sudo timedatectl set-time "{str}"')
    
    os.system('timedatectl')
    
    input("hit any key to sytem reboot")
    os.system('sudo reboot')
  except ValueError as e:
    print_operation_error(f"invalid value: {str}")
    print_usage(usage)
    return False

  print("done")
  return True



def set_keyboard(args):

  usage = "keyboard  { us | jp | hhk }"
  if args is None or len(args) == 0:
    print_usage(usage)
    return
  
  locale = args[0]
  if locale != "us" and locale != "jp" and locale != "hhk":
    print_usage(usage)
    return


  dir = os.getenv('KEY_DIR')
  res = f"{dir}/keyboard.{args[0]}"

  if os.path.exists(res) is False:
    print_error(f"file: {res} not found.")
    print_usage(usage)
    return False

  cmd = os.getenv('CHANGE_KEYBOARD_PATH')
  try:
    ret = subprocess.run([cmd, locale], capture_output=True)

    if ret.returncode == 0:
      input("hit any key to sytem reboot")
      os.system('sudo reboot')
    else:
      print_error("Failed to change keyboard layout.")
  except subprocess.CalledProcessError as e:
    logging.exception(e)
  return False
