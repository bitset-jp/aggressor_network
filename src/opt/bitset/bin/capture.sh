#!/bin/bash
if [ $# != 3 ]; then
  echo  $# > /tmp/hoge
  echo usage $0 {network interface} {save dir} {rotate_seconds}
  exit 1
fi

BASE_DIR=$(cd $(dirname $0)/..; pwd)
BIN_DIR=$BASE_DIR/bin
CONF_DIR=$BASE_DIR/conf

. $CONF_DIR/conf

dev=$1
dir=$2
sec=$3

LOG_FILE=/tmp/capture_$dev.log

date > $LOG_FILE

fname=${dir}/${dev}_%Y-%m-%d_%H-%M-%S.pcap

echo dir: $dir >> $LOG_FILE 2>&1
echo file: $fname >> $LOG_FILE 2>&1
echo sec: $sec >> $LOG_FILE 2>&1

echo start  >> $LOG_FILE 2>&1

tcpdump -n -i $dev -G $sec -s4096 -w $fname -z gzip  >> $LOG_FILE 2>&1

echo stop  >> $LOG_FILE 2>&1


# 未圧縮のファイルが残っていれば圧縮
for pcap in `ls $dir/$dev_*.pcap`;
do
  echo "gzip $pcap" >> $LOG_FILE 2>&1
  gzip $pcap
done
