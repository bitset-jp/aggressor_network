#!/bin/bash

####clear
#echo "execute $0"

BASE_DIR=$(cd $(dirname $0)/..; pwd)

BIN_DIR=$BASE_DIR/bin
CONF_DIR=$BASE_DIR/conf
APP_DIR=$BASE_DIR/app
RES_DIR=$BASE_DIR/res

. $CONF_DIR/conf

trap '' INT
trap '' TSTP
trap '' SIGUSR1
trap '' SIGUSR2

PLAYER="$APP_DIR/$APP_NAME"

cd $APP_DIR

export BASE_PATH=$APP_DIR
export BIN_DIR=$BIN_DIR
export DEV=$DEV
export BRIDGE=$BRIDGE
export MOUNT_INFO=$MOUNT_INFO
export TITLE=$TITLE
export CAPTURE_PATH=$BIN_DIR/capture.sh
export CHANGE_KEYBOARD_PATH=$BIN_DIR/set_keyboard.sh
export KEY_DIR=$RES_DIR/keyboard

clear
toilet  --filter border:metal -f future ' NETWORK  EMULATOR '
echo  -e "  copyright (c) bitset.jp 2023  \e[36m https://bitset/jp  \e[m"
echo ""

export LANG=c

while true;
do
  brctl show $BRIDGE > /dev/null
  ret=$?
  if [ $ret -eq 0 ]; then
    break
  fi
  echo "wait for bridge ..."
  sleep 2
done


while :
do
  $PLAYER 
  ret=$?
  if [ $ret = 99 ]; then
    touch $EXIT_FILE
    break
  elif [ $ret = 1 ]; then
    break
  fi
done
