# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
# author dieser
# contact dieser@163.com
import redis
import subprocess
import json
import requests
import time

url = 'http://www.baidu.com'


def checknetwork():
    try:
        response = requests.get(url, timeout=1)
        return True
    except Exception as e:
        return False


def clearoldip():
    with open("/root/ip.txt", 'r') as f:
        old_ip = f.readline()
        r = redis.Redis(host='x.x.x.x', port=63790, db=22, password='passwd')
        print(old_ip)
        r.srem('91vps', old_ip)


def redial():
    subprocess.run("/usr/sbin/pppoe-stop")
    subprocess.run("/usr/sbin/pppoe-start")
    time.sleep(1)


def getip():
    # HTTP GET
    r = requests.get('https://ipw.cn/api/ip/locate')
    #  转成 Python 字典并赋值
    ip_detail = json.loads(r.text)
    IP = ip_detail['IP']
    newip = 'str' + str(IP) + ':10240'
    with open("/root/ip.txt", 'w') as f:
        f.write(newip)


def writeiptoredis():
    r = redis.Redis(host='x.x.x.x', port=63790, db=22, password='passwd')
    with open("/root/ip.txt", 'r') as f:
        newip = f.readline()
    r.sadd('91vps', newip)
    print(newip)


if __name__ == "__main__":
    flag = False
    if checknetwork():
        clearoldip()
        flag = True
    redial()
    while not checknetwork():
        print("1111")
        redial()
    if not flag:
        clearoldip()
    getip()
    writeiptoredis()
