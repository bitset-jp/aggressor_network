#!/bin/bash
HR1='================================================================' 
HR2='----------------------------------------------------------------' 

BASE_DIR=$(cd $(dirname $0)/..; pwd)
BIN_DIR=$BASE_DIR/bin
CONF_DIR=$BASE_DIR/conf
CONSOLE_DIR=$BASE_DIR/console

cd /tmp

. $CONF_DIR/conf
. $CONSOLE_DIR/common.sh
. $CONSOLE_DIR/filter.sh
. $CONSOLE_DIR/handler.sh


function signal_handler(){
  :
}


trap signal_handler SIGINT

function show_status(){
  echo $(date +%Y-%m-%dT%H:%M:%S)
  check_bridge
  ret=$?

  if [ $ret -eq 0 ]; then
    : # echo bridge ok
  else
    echo bridge not found
  fi
}

function show_menu(){
  echo ''
  echo $HR1
  show_status
  echo $HR2
  #cat $CONSOLE_DIR/menu.txt
  #echo -e "\x1b[34m[settings]\x1b[39m"
  #tc qdisc show dev eth0
  echo -e "\x1b[34m[stat]\x1b[39m"
  tc -s qdisc show dev eth0
  echo $HR2
}

while true;
do
  check_bridge
  ret=$?
  if [ $ret -eq 0 ]; then
    break
  fi
  echo "wait for bridge ..."
  sleep 2
done

filter_init

while true;
do
  show_menu

  echo -n "input> "
  read line

  if [ -z "${line}" ]; then
    continue
  fi

  set ${line}
  cmd=${1,,}
  arg1=${2}
  arg2=${3}
  echo $cmd / $arg1 / $arg2

  if [ $cmd = "exit" ]; then
    exit
  elif [ $cmd = "help" ]; then
    menu_help
  elif [ $cmd = "mon" -o $cmd = "monitor" ]; then
    menu_monitor $arg1
  elif [ $cmd = "clear"  ]; then
    menu_clear
  elif [ $cmd = "delay"  ]; then
    menu_delay $arg1 $arg2
  elif [ $cmd = "loss"  ]; then
    menu_loss $arg1
  fi
done
