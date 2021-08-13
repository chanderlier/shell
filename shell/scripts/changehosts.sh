#!/bin/bash
# 将ping出来的IP及其对应的域名写入到/etc/hosts中
N20=`ping v9-z.douyinvod.com -c 1 -w 1 | sed '1{s/[^(]*(//;s/).*//;q}'`
sed -i '/douyinpic/d' /etc/hosts
echo "$N20 p1.douyinpic.com" >> /etc/hosts