# -*- coding: utf-8 -*-

import logging

def print_usage(msg):
  print(f"USAGE: {msg}")


def print_error(msg):
  print(f"\x1b[33;1mERROR: {msg}\x1b[0m")
  logging.error(msg)


def print_operation_error(msg):
  print(f"\x1b[33;1mERROR: {msg}\x1b[0m")
