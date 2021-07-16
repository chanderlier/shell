# -*- coding: utf-8 -*-
# author dieser
# 获取指定ecsid的IP地址，并写入到redis中
import os
import sys
import ast
import redis
import json
from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models


os.chdir("/alidata/scripts/singapore")


def clearoldiplist():
    r = redis.Redis(host='domain', port=63790, db=0, password='passwd')
    r.delete('ali_proxies')
    r.delete('ali_proxies_2')


def writeiptoredis1():
    r = redis.Redis(host='domain', port=63790, db=0, password='passwd')
    with open('eiplist1.txt', 'r') as f:
        iplist = f.readlines()
        iplists = [x.strip() for x in iplist if x.strip() != ""]
        for i in iplists:
            r.sadd('ali_proxies', i)


def writeiptoredis2():
    r = redis.Redis(host='domain', port=63790, db=0, password='passwd')
    with open('eiplist2.txt', 'r') as f:
        iplist = f.readlines()
        iplists = [x.strip() for x in iplist if x.strip() != ""]
        for i in iplists:
            r.sadd('ali_proxies_2', i)


def truncatefile(file):
    with open(file, 'w') as f:
        f.truncate()


def truncatefiles():
    truncatefile('ecsiplist1.txt')
    truncatefile('ecsiplist2.txt')
    truncatefile('eiplist1.json')
    truncatefile('eiplist1.json')


with open('ecsidlist1.txt', 'r') as f:
    ecsid1 = f.readlines()
    ecsidlist1 = [x.strip() for x in ecsid1 if x.strip() != '']

with open('ecsidlist2.txt', 'r') as f:
    ecsid2 = f.readlines()
    ecsidlist2 = [x.strip() for x in ecsid2 if x.strip() != '']


def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
        data_dict = ast.literal_eval(data)
    return data_dict


def parse_data(data_dict, filename):
    data_counts = len(data_dict.get('body').get('NetworkInterfaceSets').get('NetworkInterfaceSet'))
    for item in range(data_counts):
        temp_list = []
        ip = data_dict.get('body').get('NetworkInterfaceSets').get('NetworkInterfaceSet')[item].get('AssociatedPublicIp').get('PublicIpAddress')
        temp_list.append(ip)
        with open(filename, 'a') as f:
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
            access_key_id='xxxx',
            access_key_secret='xxxx',
        )
        config.endpoint = 'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)


class proxies1:
    def __init__(self):
        pass

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = aliclient.create_client('accessKeyId', 'accessKeySecret')
        for i in range(len(ecsidlist1)):
            describe_network_interfaces_request = ecs_20140526_models.DescribeNetworkInterfacesRequest(
                region_id='ap-southeast-1',
                instance_id=ecsidlist1[i]
            )
            client.describe_network_interfaces(describe_network_interfaces_request)
            data = client.describe_network_interfaces(describe_network_interfaces_request)
            with open('eiplist1.json', 'w') as f:
                print(data, file=f)
            data_dict = read_file('eiplist1.json')
            parse_data(data_dict, 'ecsiplist1.txt')

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = aliclient.create_client('accessKeyId', 'accessKeySecret')
        for i in range(len(ecsidlist1)):
            describe_network_interfaces_request = ecs_20140526_models.DescribeNetworkInterfacesRequest(
                region_id='ap-southeast-1',
                instance_id=ecsidlist1[i]
            )
            client.describe_network_interfaces(describe_network_interfaces_request)
            data = client.describe_network_interfaces(describe_network_interfaces_request)
            with open('eiplist1.json', 'w') as f:
                print(data, file=f)
            data_dict = read_file('eiplist1.json')
            parse_data(data_dict, 'ecsiplist1.txt')

        await client.describe_network_interfaces_async(describe_network_interfaces_request)


class proxies2:
    def __init__(self):
        pass

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = aliclient.create_client('accessKeyId', 'accessKeySecret')
        for i in range(len(ecsidlist2)):
            describe_network_interfaces_request = ecs_20140526_models.DescribeNetworkInterfacesRequest(
                region_id='ap-southeast-1',
                instance_id=ecsidlist2[i]
            )
            client.describe_network_interfaces(describe_network_interfaces_request)
            data = client.describe_network_interfaces(describe_network_interfaces_request)
            with open('plist2.json', 'w') as f:
                print(data, file=f)
            data_dict = read_file('eiplist2.json')
            parse_data(data_dict, 'ecsiplist2.txt')

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = aliclient.create_client('accessKeyId', 'accessKeySecret')
        for i in range(len(ecsidlist2)):
            describe_network_interfaces_request = ecs_20140526_models.DescribeNetworkInterfacesRequest(
                region_id='ap-southeast-1',
                instance_id=ecsidlist2[i]
            )
            client.describe_network_interfaces(describe_network_interfaces_request)
            data = client.describe_network_interfaces(describe_network_interfaces_request)
            with open('eiplist2.json', 'w') as f:
                print(data, file=f)
            data_dict = read_file('eiplist2.json')
            parse_data(data_dict, 'ecsiplist2.txt')

        await client.describe_network_interfaces_async(describe_network_interfaces_request)


if __name__ == '__main__':
    truncatefiles()
    proxies1.main(sys.argv[1:])
    proxies2.main(sys.argv[1:])
    clearoldiplist()
    writeiptoredis1()
    writeiptoredis2()
