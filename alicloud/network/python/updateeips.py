# author dieser
# 将阿里云指定地域的IP写入到redis中,并将更新信息发送到指定邮件接收者
import sys
import ast
import sys
import os
import json
import redis
import smtplib
from typing import List
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_vpc20160428.client import Client as Vpc20160428Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_vpc20160428 import models as vpc_20160428_models
from email.mime.text import MIMEText
from email.header import Header


def sendupdatemsg():
    mail_host = "smtp.exmail.qq.com"
    mail_user = "senderemail"  # 发送者邮件地址
    mail_pass = "passwd"  # 口令
    receivers = ['receiveremail']  # 接收者邮件地址
    sum = 400
    success = 20
    fail = 0
    unsign = 0
    text = """
阿里云更新EIP情况如下
现有EIP总量: %d
更新成功: %d
更新失败: %d
存在未绑定的EIP: %d""" % (sum, success, fail, unsign)
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("阿里云", 'utf-8')
    message['To'] = Header("运维", 'utf-8')
    message['Subject'] = Header('阿里云更新EIP情况通知', 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, receivers, message.as_string())
        print("Send Mail Success")
    except Exception as e:
        print(e)
        print("Error: Send Mail Faild")


os.chdir("/alidata/scripts")


def clearoldiplist():
    r = redis.Redis(host='10.0.3.100', port=6379, db=7, password='passwd')
    r.delete('ali_proxies')


def writeiptoredis():
    r = redis.Redis(host='10.0.3.100', port=6379, db=7, password='passwd')
    with open('eiplist.txt', 'r') as f:
        iplist = f.readlines()
        iplists = ['targetsocial:passwd@' + x.strip() + ':10240' for x in iplist if x.strip() != ""]
        # requests.post('http://10.0.11.202:8888', json={"ip_list": iplists})
        for i in iplists:
            r.sadd('ali_proxies', i)


def truncatefile():
    f = open('eiplist.txt', 'w')
    f.truncate()
    f.close()


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()
        data_dict = ast.literal_eval(data)
    return data_dict


def parse_data(data_dict):
    data_counts = len(data_dict.get('body').get('EipAddresses').get('EipAddress'))
    for item in range(data_counts):
        temp_list = []
        ip = data_dict.get('body').get('EipAddresses').get('EipAddress')[item].get('IpAddress')
        temp_list.append(ip)
        with open('eiplist.txt', 'a') as f:
            f.write('-'.join(temp_list) + '\n')


class aliclient:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:

        config = open_api_models.Config(
            access_key_id='ak',
            access_key_secret='sk',
        )
        config.endpoint = 'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def main(
        args: List[str], page, filename
    ) -> None:
        client = aliclient.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-qingdao',
            page_size=100,
            page_number=page
        )
        client.describe_eip_addresses(describe_eip_addresses_request)
        eip_json = client.describe_eip_addresses(describe_eip_addresses_request)
        with open(filename, 'w') as f:
            print(eip_json, file=f)

    @staticmethod
    async def main_async(
        args: List[str], page, filename
    ) -> None:
        client = aliclient.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-qingdao',
            page_size=100,
            page_number=page
        )
        await client.describe_eip_addresses_async(describe_eip_addresses_request)
        eip_json = client.describe_eip_addresses(describe_eip_addresses_request)
        with open(filename, 'w') as f:
            print(eip_json, file=f)


class geteipid:
    def __init__(self):
        pass

    @staticmethod
    def main(
        args: List[str], page, filename
    ) -> None:
        client = aliclient.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = ecs_20140526_models.DescribeEipAddressesRequest(
            region_id='cn-qingdao',
            status='Available',
            page_number=page,
            page_size=100
        )
        client.describe_eip_addresses(describe_eip_addresses_request)
        eipid_json = client.describe_eip_addresses(describe_eip_addresses_request)
        with open(filename, 'w') as f:
            print(eipid_json, file=f)

    @staticmethod
    async def main_async(
        args: List[str], page, filename
    ) -> None:
        client = aliclient.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = ecs_20140526_models.DescribeEipAddressesRequest(
            region_id='cn-qingdao',
            status='Available',
            page_number=page,
            page_size=100
        )
        await client.describe_eip_addresses_async(describe_eip_addresses_request)
        eipid_json = client.describe_eip_addresses(describe_eip_addresses_request)
        with open(filename, 'w') as f:
            print(eipid_json, file=f)


if __name__ == '__main__':
    Sample.main(sys.argv[1:], 1, 'eiplist.json')
    Sample.main(sys.argv[1:], 2, 'eiplist_2.json')
    Sample.main(sys.argv[1:], 3, 'eiplist_3.json')
    Sample.main(sys.argv[1:], 4, 'eiplist_4.json')
    truncatefile()
    data_dict = read_file('eiplist.json')
    parse_data(data_dict)
    data_dict = read_file('eiplist_2.json')
    parse_data(data_dict)
    data_dict = read_file('eiplist_3.json')
    parse_data(data_dict)
    data_dict = read_file('eiplist_4.json')
    geteipid.main(sys.argv[1:], 1, 'eipidlist.json')
    parse_data(data_dict)
    data_dict = read_file('eipidlist.json')
    parse_data(data_dict)
    # data_dict=read_file('eiplist_5.json')
    # parse_data(data_dict)
    clearoldiplist()
    writeiptoredis()
    sendupdatemsg()
