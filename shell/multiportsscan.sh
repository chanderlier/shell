#!/bin/bash

for server in `more server_list.txt`
do
        for port in `more port_list.txt`
        do
                #echo $server
                nc -zvw3 $server $port
                echo ""

        done
done