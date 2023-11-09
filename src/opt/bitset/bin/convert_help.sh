#!/bin/bash

BASE_DIR=$(cd $(dirname $0)/..; pwd)
BIN_DIR=$BASE_DIR/bin
APP_DIR=$BASE_DIR/app
RES_DIR=$BASE_DIR/res
HELP_DIR=$RES_DIR/help

for file in $HELP_DIR/*.html; do

  dist=/tmp/$(basename $file)

  #echo $dist
  rm -f $dist
  if [ ! -e $dist ]; then
    cat  $file | \
    sed 's/<t>/\\t/g' | \
    sed 's/<t2>/\\t\\t/g' | \
    sed 's/<t3>/\\t\\t\\t/g' | \
    sed 's/<t4>/\\t\\t\\t\\t/g' | \
    sed 's/<t5>/\\t\\t\\t\\t\\t/g' | \
    sed 's/<t6>/\\t\\t\\t\\t\\t\\t/g' | \
    sed 's/<t7>/\\t\\t\\t\\t\\t\\t\\t/g' | \
    sed 's/<t8>/\\t\\t\\t\\t\\t\\t\\t\\t/g' | \
    sed 's/<n>/\\n/g'| \
    sed 's/<s>/\\x1b[1C/g'| \
    sed 's/<s2>/\\x1b[2C/g'| \
    sed 's/<s4>/\\x1b[4C/g'| \
    sed 's/<s6>/\\x1b[6C/g'| \
    sed 's/<s8>/\\x1b[8C/g'| \
    sed 's/<red>/\\x1b[31m/g'| \
    sed 's/<green>/\\x1b[32m/g'| \
    sed 's/<yellow>/\\x1b[33m/g'| \
    sed 's/<blue>/\\x1b[34m/g'| \
    sed 's/<magenta>/\\x1b[35m/g'| \
    sed 's/<cyan>/\\x1b[36m/g'| \
    sed 's/<white>/\\x1b[37m/g'| \
    sed 's/<byellow>/\\x1b[43m/g'| \
    sed 's/<b>/\\x1b[1m/g' | \
    sed 's/<u>/\\x1b[4m/g' | \
    sed 's/<r>/\\x1b[7m/g' | \
    sed 's/<\/>/\\x1b[0m/g' > $dist
  fi
done
