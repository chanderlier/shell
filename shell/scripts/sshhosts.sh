#!/bin/bash
set -e
HOSTS='10.0.10.177'
for host in $HOSTS;do
    echo $host
    ssh root@$host "echo 1" 
    if [ 'echo "$?"' = "0"];then
        echo "nice"
        ssh root@$host "touch /root/123lalala.txt"
    else
        echo "$host cannot be connected"
    fi
done 