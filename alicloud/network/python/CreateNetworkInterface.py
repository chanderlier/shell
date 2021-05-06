# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
# 运行脚本，批量创建辅助弹性网卡,弹性网卡数量由networkinterface_numbers指定，该弹性网卡仅包含一个IP地址
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret
        )
        config.endpoint = 'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        networkinterface_numbers = 100
        for i in range(len(networkinterface_numbers)):
            create_network_interface_request = ecs_20140526_models.CreateNetworkInterfaceRequest(
                region_id='cn-shanghai',
                v_switch_id='vsw-uf6fokgzfvpkjryb774sa',
                security_group_id='sg-uf68lxrsj3h2ru2w8pf4',
                # secondary_private_ip_address_count=1
            )
            client.create_network_interface(create_network_interface_request)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        networkinterface_numbers = 100
        for i in range(len(networkinterface_numbers)):
            create_network_interface_request = ecs_20140526_models.CreateNetworkInterfaceRequest(
                region_id='cn-shanghai',
                v_switch_id='vsw-uf6fokgzfvpkjryb774sa',
                security_group_id='sg-uf68lxrsj3h2ru2w8pf4',
                # secondary_private_ip_address_count=1
            )
            await client.create_network_interface_async(create_network_interface_request)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
