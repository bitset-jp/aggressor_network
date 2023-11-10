#!/bin/bash
#
# Framebuffer recorder
#
if [ $# -ne 2 ]; then
  echo "usage:"
  echo "  $ /PATH/TO/fbrec.sh  [Output Path] [Recording Time(sec)]"
  echo "example:"
  echo "  $ fbrec.sh /tmp 10"
  exit
fi
dst=$1
max_time=$2

echo output: $dst
echo rec time:  $max_time

function capture (){
  ppm=$dst/ss_`date +%Y%m%d-%T | tr -d :`_$1.ppm
  echo $ppm
  fbcat | gzip -c > $ppm.gz
}

start_time=$(date "+%s")
elapsed_time=0
no=0

while [ $elapsed_time -lt $max_time ]
do
  let no=$no+1
  capture $no 
  current_time=$(date "+%s")
  elapsed_time=$(($current_time - $start_time)) 
  #sleep $interval
done 
