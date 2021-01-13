#!/bin/env python
# -*- coding: utf8 -*-

import sys
import nmap
import json


def scaner(port):
    open_ips = []
    close_ips = []
    nm = nmap.PortScanner()
    hosts = '192.168.1.0/20'
    scan = nm.scan(hosts, '22, ' + port, '-sV')
    for ip in nm.all_hosts():
        if nm[ip]['tcp'][22]['state'] != 'closed':
            if nm[ip]['tcp'][int(port)]['state'] == 'open':
                print(ip)
                open_ips.append(ip)
            else:
                close_ips.append(ip)
    return open_ips


if __name__ == '__main__':
    port = sys.argv[1]
    scaner(port)
