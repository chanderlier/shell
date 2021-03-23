# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models


with open('nilist.txt', 'r') as f:
    niid = f.readlines()
    nilist = [x.strip() for x in niid if x.strip() != '']


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
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        for i in range(len(nilist)):
            unassign_private_ip_addresses_request = ecs_20140526_models.UnassignPrivateIpAddressesRequest(
                region_id='cn-shanghai',
                network_interface_id=nilist[i]
            )
        # 复制代码运行请自行打印 API 的返回值
        client.unassign_private_ip_addresses(unassign_private_ip_addresses_request)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        for i in range(len(nilist)):
            unassign_private_ip_addresses_request = ecs_20140526_models.UnassignPrivateIpAddressesRequest(
                region_id='cn-shanghai',
                network_interface_id=nilist[i]
            )
        # 复制代码运行请自行打印 API 的返回值
            await client.unassign_private_ip_addresses_async(unassign_private_ip_addresses_request)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
