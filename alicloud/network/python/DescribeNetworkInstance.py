# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
# 获取指定地区，指定弹性网卡的ID信息，写入到nilist.txt中
import sys
import ast
from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models


def truncatefile():
    with open('nilist.txt', 'w') as f:
        f.truncate()


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()
        data_dict = ast.literal_eval(data)
    return data_dict


def parse_data(data_dict):
    datalist = data_dict.get('body').get('NetworkInterfaceSets').get('NetworkInterfaceSet')
    datalen = len(datalist)
    for item in range(datalen):
        templist = []
        templist.append(datalist[i].get('NetworkInterfaceId'))
        with open('nilist.txt', 'a') as f:
            f.write('-'.join(templist) + '\n')


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id='xxx',
            # 您的AccessKey Secret,
            access_key_secret='xxx',
        )
        # 访问的域名
        config.endpoint = 'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_network_interfaces_request = ecs_20140526_models.DescribeNetworkInterfacesRequest(
            region_id='cn-shanghai',
            page_size=100
        )
        # 复制代码运行请自行打印 API 的返回值
        client.describe_network_interfaces(describe_network_interfaces_request)
        data = client.describe_network_interfaces(describe_network_interfaces_request)
        with open('networkinterface.json', 'w') as f:
            print(data, file=f)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_network_interfaces_request = ecs_20140526_models.DescribeNetworkInterfacesRequest(
            region_id='cn-shanghai',
            page_size=100
        )
        # 复制代码运行请自行打印 API 的返回值
        await client.describe_network_interfaces_async(describe_network_interfaces_request)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
    truncatefile()
    data_dict = read_file('networkinterface.json')
    parse_data(data_dict)
