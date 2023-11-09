#!/usr/bin/env python3
import os
import subprocess
import logging
import time
from common import *
from enum import Enum

class CaputureMode(Enum):
  stop   = 0
  run   = 1

capture_mode = CaputureMode.stop

capture_path = os.getenv('CAPTURE_PATH')

pid = [0,0]

def start_capture(devs, path, sec ):
  global pid
  global capture_mode

  if is_running():
    print_error("already capturing")
    return

  pid = [0,0]
  

  if sec is None:
    sec = 600

  for dev in devs:
    print(f"start capture {dev} {sec}")

    cmd = f"{capture_path}  {dev}  {path}  {sec}"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #print("PID:", process.pid)

    index = 0 if dev == "eth0" else 1
    pid[index] = process.pid

    time.sleep(0.5)

  if pid[0] != 0 or pid[1] != 0:
    capture_mode = CaputureMode.run


def stop_capture():
  global pid
  global capture_mode

  capture_mode = CaputureMode.stop

  if is_running():
    print("stop caputure")
    os.system('pkill tcpdump')
    time.sleep(1)

    print("waiting for caputure stop...")

    for i in range(600):
      if is_running() == False:
        print("...stopped")
        break
      time.sleep(0.1)
  else:
    print_operation_error("not in capture")        


def is_capture_mode():
  return True if capture_mode == CaputureMode.run else False

def is_running():
  return True if pid[0] != 0 or pid[1] != 0 else False


def notify_sigchld(index):
  global pid

  pid[index] = 0


def pids():
  return (pid[0] ,pid[1])

def status():
  return (0 < pid[0] , 0 < pid[1])

