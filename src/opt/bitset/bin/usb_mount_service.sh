#!/bin/sh
# @see https://wiki.archlinux.jp/index.php/Udisks
# @see http://storaged.org/doc/udisks2-api/
# @see https://gihyo.jp/admin/serial/01/ubuntu-recipe/0559
#
#
BASE_DIR=$(cd $(dirname $0)/..; pwd)
CONF_DIR=$BASE_DIR/conf
. $CONF_DIR/conf

UDISK_RESULT=/tmp/udisk_result
LOG_FILE=/tmp/mount.log

echo start > $LOG_FILE

pathtoname() {
    udevadm info -p /sys/"$1" | awk -v FS== '/DEVNAME/ {print $2}'
}

stdbuf -oL -- udevadm monitor --udev -s block | while read -r -- _ _ event devpath _; do

    if [ "$event" = add ]; then
        devname=$(pathtoname "$devpath")
        udisksctl mount --block-device "$devname"  --no-user-interaction > $UDISK_RESULT
        ret=$?

        if [ $ret -eq 0 ]; then
            echo add: $devname >> $LOG_FILE 2>&1

            cat $UDISK_RESULT | cut -d " " -f 4 > $MOUNT_INFO

            echo `cat $MOUNT_INFO` >> $LOG_FILE 2>&1

            /usr/bin/pkill -SIGUSR1 -f $APP_NAME
        fi
    elif [ "$event" = remove ]; then
        if [ -e $MOUNT_INFO ]; then
            echo remove: `cat $MOUNT_INFO` >> $LOG_FILE 2>&1
            rm -f $MOUNT_INFO
            /usr/bin/pkill -SIGUSR2 -f $APP_NAME
        fi    
    fi        
done
