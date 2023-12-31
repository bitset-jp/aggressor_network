#!/bin/bash

BASE_DIR=$(cd $(dirname $0)/..; pwd)
BIN_DIR=$BASE_DIR/bin
APP_DIR=$BASE_DIR/app
RES_DIR=$BASE_DIR/res
KEY_DIR=$RES_DIR/keyboard

LOG_FILE=/tmp/keyboard.log

dst=/etc/default/keyboard
res=$KEY_DIR/keyboard.$1


echo $res > $LOG_FILE 2>&1

if [ ! -e $res ]; then
  echo "ERR: not found $res" >> $LOG_FILE 2>&1
  exit 1
fi

sudo mount -o remount,rw /
sudo mount -o remount,rw /boot

sudo rm $dst >> $LOG_FILE 2>&1
sudo ln -s $res $dst >> $LOG_FILE 2>&1
touch $res
sudo /etc/init.d/console-setup.sh restart

sudo mount -o remount,ro /
sudo mount -o remount,ro /boot
exit 0

