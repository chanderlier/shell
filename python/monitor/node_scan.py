#!/bin/env python
# -*- coding: utf8 -*-

import nmap
import json
import requests


alert_template = """
告警程序: AlertManager 
未安装 NodeExporter 的主机: {} 
"""


def send_message_by_qyapi(content):
    lost_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key='
    headers = {"Content-Type": "text/plain"}
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        }
    }
    res = requests.post(url=lost_url, data=json.dumps(data), headers=headers)
    print(res.text)


# 扫描出全部的开放 9100 端口的主机
def scaner():
    open_ips = []
    close_ips = []
    nm = nmap.PortScanner()
    hosts = '192.168.1.0/20'
    scan = nm.scan(hosts, '22, 9100', '-sV')
    for ip in nm.all_hosts():
        if nm[ip]['tcp'][22]['state'] != 'closed':
            if nm[ip]['tcp'][9100]['state'] == 'open':
                open_ips.append(ip)
            else:
                close_ips.append(ip)

    close_ips = [ip for ip in close_ips if ip.split('.')[2] not in ['14', '15']]
    msg = alert_template.format(str(close_ips))
    send_message_by_qyapi(msg)
    return open_ips


# 将主机添加到 Prometheus 的配置文件中，动态更新
def adder(ips=None):
    gen_hosts = []
    for ip in ips:
        item = {'targets': [ip + ':9100'], 'labels': {'instance': ip}}
        print("Add The Host of {}\n".format(ip))
        gen_hosts.append(item)

    with open('hosts.json', 'w+') as fb:
        fb.write(json.dumps(gen_hosts))


if __name__ == '__main__':
    ips = scaner()
    adder(ips)
