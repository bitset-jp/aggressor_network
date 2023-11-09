#!/bin/bash
BASE_DIR=$(cd $(dirname $0)/..; pwd)
BIN_DIR=$BASE_DIR/bin
CONF_DIR=$BASE_DIR/conf

. $CONF_DIR/conf


$BIN_DIR/convert_help.sh 2> /tmp/convert.log 

rm -f $EXIT_FILE

while :
do
  tmux new-session  $BIN_DIR/setup_tmux.sh
  if [ -e $EXIT_FILE ]; then
    rm -f $EXIT_FILE
    break
  fi

  echo wait... 3
  sleep 1
  echo wait... 2
  sleep 1
  echo wait... 1
  sleep 1
done

