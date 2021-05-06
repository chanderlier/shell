# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
# 删除指定文件中的弹性网卡
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models

# 打开网卡列表文件，将信息写入到nilist列表中
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
        config = open_api_models.Config(
            access_key_id='xxx',
            access_key_secret='xxx'
        )
        config.endpoint = 'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        # 删除nilist中的弹性网卡
        for i in range(len(nilist)):
            delete_network_interface_request = ecs_20140526_models.DeleteNetworkInterfaceRequest(
                region_id='cn-shanghai',
                network_interface_id=nilist[i]
            )
            client.delete_network_interface(delete_network_interface_request)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        for i in range(len(nilist)):
            delete_network_interface_request = ecs_20140526_models.DeleteNetworkInterfaceRequest(
                region_id='cn-shanghai',
                network_interface_id=nilist[i]
            )
            await client.delete_network_interface_async(delete_network_interface_request)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
