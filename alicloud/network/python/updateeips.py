# author dieser
# 将阿里云指定地域的IP写入到redis中
import sys
import ast
import sys
import os
import json
import redis
from typing import List
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_vpc20160428.client import Client as Vpc20160428Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_vpc20160428 import models as vpc_20160428_models

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
    parse_data(data_dict)
    # data_dict=read_file('eiplist_5.json')
    # parse_data(data_dict)
    clearoldiplist()
    writeiptoredis()
