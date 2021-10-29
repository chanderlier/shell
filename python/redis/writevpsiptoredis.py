# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
# author dieser
# contact dieser@163.com
# 将VPS的拨号IP写入到指定redis中
import redis
import subprocess
import json
import requests
import time
import socket

url = 'http://www.baidu.com'
# 获取主机名
hostname = socket.gethostname()


def checknetwork():
    try:
        response = requests.get(url, timeout=1)
        return True
    except Exception as e:
        return False


def redial():
    subprocess.Popen("/usr/sbin/pppoe-stop")
    subprocess.Popen("/usr/sbin/pppoe-start")
    time.sleep(1)


def getip():
    # HTTP GET
    r = requests.get('https://ipw.cn/api/ip/locate')
    #  转成 Python 字典并赋值
    ip_detail = json.loads(r.text)
    IP = ip_detail['IP']
    newip = 'auth_passwd' + str(IP) + ':10240'
    with open("/root/ip.txt", 'w') as f:
        f.write(newip)


def writeiptoredis(expire):
    r = redis.Redis(host='ip', port=63790, db=22, password='passwd')
    with open("/root/ip.txt", 'r') as f:
        newip = f.readline()
    r.set('ip:vps:' + hostname, newip, ex=expire)
    print(newip)


if __name__ == "__main__":
    flag = False
    st = int(time.time())
    if checknetwork():
        flag = True
    redial()
    while not checknetwork():
        print("1111")
        redial()
    et = int(time.time())
    expire = 300 - (et - st)
    getip()
    writeiptoredis(expire)
