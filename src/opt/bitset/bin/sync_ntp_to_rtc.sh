#/bin/bash

SERVER=ntp.nict.jp

sudo ntpdate $SERVER

echo "sync to RTC"

sudo hwclock --systohc
timedatectl
