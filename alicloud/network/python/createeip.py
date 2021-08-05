# 创建指定数量的EIP，将未绑定的EIP写入到eipidlist.txt中
import sys
import ast
import sys
import os
import json
from typing import List
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models

os.chdir("/root/aliyun-vpc")


def truncatefile():
    f = open('eipidlist.txt', 'w')
    f.truncate()


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()
        data_dict = ast.literal_eval(data)
    return data_dict


def parse_data(data_dict):
    data_counts = len(data_dict.get('body').get('EipAddresses').get('EipAddress'))
    print(data_counts)
    for item in range(data_counts):
        temp_list = []
        ip = data_dict.get('body').get('EipAddresses').get('EipAddress')[item].get('AllocationId')
        temp_list.append(ip)
        with open('eipidlist.txt', 'a') as f:
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
            access_key_id='passwd',
            access_key_secret='passwd',
        )
        config.endpoint = 'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)


class createeip:
    def __init__(self):
        pass

    @staticmethod
    def main(
        args: List[str], eipnumber,
    ) -> None:
        client = aliclient.create_client('accessKeyId', 'accessKeySecret')
        allocate_eip_address_request = ecs_20140526_models.AllocateEipAddressRequest(
            bandwidth='3',
            region_id='cn-qingdao'
        )
        for i in range(eipnumber):
            client.allocate_eip_address(allocate_eip_address_request)

    @staticmethod
    async def main_async(
        args: List[str], eipnumber
    ) -> None:
        client = aliclient.create_client('accessKeyId', 'accessKeySecret')
        allocate_eip_address_request = ecs_20140526_models.AllocateEipAddressRequest(
            bandwidth='3',
            region_id='cn-qingdao'
        )
        for i in range(eipnumber):
            await client.allocate_eip_address_async(allocate_eip_address_request)


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
    # createeip.main(sys.argv[1:], 196)
    geteipid.main(sys.argv[1:], 1, 'eipidlist1.json')
    truncatefile()
    data_dict = read_file('eipidlist1.json')
    parse_data(data_dict)
    geteipid.main(sys.argv[1:], 2, 'eipidlist2.json')
    data_dict = read_file('eipidlist2.json')
    parse_data(data_dict)
