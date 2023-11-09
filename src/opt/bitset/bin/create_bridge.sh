#/bin/bash

BASE_DIR=$(cd $(dirname $0)/..; pwd)
BIN_DIR=$BASE_DIR/bin
CONF_DIR=$BASE_DIR/conf

. $CONF_DIR/conf

log=$LOG_DIR/create_bridge.log

echo $(date +%Y-%m-%dT%H:%M:%S) : execute $0

brctl show $BRIDGE > /dev/null
ret=$?
if [ $ret -eq 0 ]; then
  echo "found bridge: $BRIDGE (skip)"
  exit
fi

echo "create bridge: $BRIDGE"

brctl addbr $BRIDGE 

for NIC in $NICS
do
  ip addr flush dev $NIC

  while :
  do
    brctl addif $BRIDGE $NIC
    ret=$?
    if [ $ret -eq 0 ]; then
      echo "add interface: $NIC"
      break
    fi
    sleep 2
  done
done

for NIC in $NICS
do
  ip link set dev $NIC promisc on
  ip link set dev $NIC up 
done
ip link set dev $BRIDGE up  

brctl show $BRIDGE
echo $(date +%Y-%m-%dT%H:%M:%S) : finish $0
