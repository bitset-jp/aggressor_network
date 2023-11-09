#!/bin/bash

BASE_DIR=$(cd $(dirname $0)/..; pwd)
BIN_DIR=$BASE_DIR/bin
APP_DIR=$BASE_DIR/app
RES_DIR=$BASE_DIR/res
HELP_DIR=$RES_DIR/help

helpfile=/tmp/help.html

tabs -2
clear
err=0
if [ $# = 1 ]; then
  if [ $1 = "0" -o $1 = "1" -o $1 = "a" ]; then
    helpfile=/tmp/select.html
  else
    helpfile=/tmp/$1.html
  fi
  if [ ! -e $helpfile ]; then
    err=1
    helpfile=/tmp/help.html
  fi
fi

echo -e $(cat $helpfile)

if [ $err = 1 ]; then
  echo -e "\x1b[31m\x1b[1m*** ERR: invalid keyword: \x1b[33m$1\x1b[0m"
fi




