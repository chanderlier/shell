# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys
import os
import json
import ast
import redis
import requests
from typing import List
from alibabacloud_vpc20160428.client import Client as Vpc20160428Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_vpc20160428 import models as vpc_20160428_models


os.chdir("/alidata/scripts")


def clearoldiplist():
    r = redis.Redis(host='10.0.3.100', port=6379, db=7, password='RedisPassword')
    r.delete('ali_proxies')


def writeiptoredis():
    r = redis.Redis(host='10.0.3.100', port=6379, db=7, password='RedisPassword')
    with open('eiplist.txt', 'r') as f:
        iplist = f.readlines()
        iplists = ['squidpasswd' + x.strip() + ':10240' for x in iplist if x.strip() != ""]
        requests.post('http://10.0.11.202:8888', json={"ip_list": iplists})
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


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Vpc20160428Client:
        config = open_api_models.Config(
            access_key_id='access_key_id',
            access_key_secret='access_key_secret',
        )
        # 访问的域名
        config.endpoint = 'vpc.aliyuncs.com'
        return Vpc20160428Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-qingdao',
            page_size=100,
            page_number=1
        )
        client.describe_eip_addresses(describe_eip_addresses_request)
        eip_json = client.describe_eip_addresses(describe_eip_addresses_request)
        with open('eiplist.json', 'w') as f:
            print(eip_json, file=f)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-qingdao',
            page_size=100,
            page_number=1
        )
        await client.describe_eip_addresses_async(describe_eip_addresses_request)


class Sample2:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Vpc20160428Client:
        config = open_api_models.Config(
            access_key_id='access_key_id',
            access_key_secret='access_key_secret',
        )
        config.endpoint = 'vpc.aliyuncs.com'
        return Vpc20160428Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-qingdao',
            page_size=100,
            page_number=2
        )
        client.describe_eip_addresses(describe_eip_addresses_request)
        eip_json = client.describe_eip_addresses(describe_eip_addresses_request)
        with open('eiplist_2.json', 'w') as f:
            print(eip_json, file=f)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-qingdao',
            page_size=100,
            page_number=2
        )
        await client.describe_eip_addresses_async(describe_eip_addresses_request)


class Sample3:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Vpc20160428Client:
        config = open_api_models.Config(
            access_key_id='access_key_id',
            access_key_secret='access_key_secret',
        )
        config.endpoint = 'vpc.aliyuncs.com'
        return Vpc20160428Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-qingdao',
            page_size=100,
            page_number=3
        )
        client.describe_eip_addresses(describe_eip_addresses_request)
        eip_json = client.describe_eip_addresses(describe_eip_addresses_request)
        with open('eiplist_3.json', 'w') as f:
            print(eip_json, file=f)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-qingdao',
            page_size=100,
            page_number=3
        )
        await client.describe_eip_addresses_async(describe_eip_addresses_request)


class Sample4:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Vpc20160428Client:
        config = open_api_models.Config(
            access_key_id='access_key_id',
            access_key_secret='access_key_secret',
        )
        config.endpoint = 'vpc.aliyuncs.com'
        return Vpc20160428Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-shanghai',
            page_size=100,
            page_number=1
        )
        client.describe_eip_addresses(describe_eip_addresses_request)
        eip_json = client.describe_eip_addresses(describe_eip_addresses_request)
        with open('eiplist_4.json', 'w') as f:
            print(eip_json, file=f)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-shanghai',
            page_size=100,
            page_number=1
        )
        await client.describe_eip_addresses_async(describe_eip_addresses_request)


class Sample5:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Vpc20160428Client:
        config = open_api_models.Config(
            access_key_id='access_key_id',
            access_key_secret='access_key_secret',
        )
        config.endpoint = 'vpc.aliyuncs.com'
        return Vpc20160428Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-shanghai',
            page_size=100,
            page_number=2
        )
        client.describe_eip_addresses(describe_eip_addresses_request)
        eip_json = client.describe_eip_addresses(describe_eip_addresses_request)
        with open('eiplist_5.json', 'w') as f:
            print(eip_json, file=f)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='cn-shanghai',
            page_size=100,
            page_number=2
        )
        await client.describe_eip_addresses_async(describe_eip_addresses_request)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
    Sample2.main(sys.argv[1:])
    Sample3.main(sys.argv[1:])
    Sample4.main(sys.argv[1:])
    Sample5.main(sys.argv[1:])
    truncatefile()
    data_dict = read_file('eiplist.json')
    parse_data(data_dict)
    data_dict = read_file('eiplist_2.json')
    parse_data(data_dict)
    data_dict = read_file('eiplist_3.json')
    parse_data(data_dict)
    data_dict = read_file('eiplist_4.json')
    parse_data(data_dict)
    data_dict = read_file('eiplist_5.json')
    parse_data(data_dict)
    clearoldiplist()
    writeiptoredis()
