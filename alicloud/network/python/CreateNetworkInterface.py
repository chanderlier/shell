# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
# 运行脚本，批量创建辅助弹性网卡
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
        create_network_interface_request = ecs_20140526_models.CreateNetworkInterfaceRequest(
            region_id='cn-shanghai',
            v_switch_id='vsw-uf6fokgzfvpkjryb774sa',
            security_group_id='sg-uf68lxrsj3h2ru2w8pf4',
            secondary_private_ip_address_count=1
        )
        # 复制代码运行请自行打印 API 的返回值
        client.create_network_interface(create_network_interface_request)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        create_network_interface_request = ecs_20140526_models.CreateNetworkInterfaceRequest(
            region_id='cn-shanghai',
            v_switch_id='vsw-uf6fokgzfvpkjryb774sa',
            security_group_id='sg-uf68lxrsj3h2ru2w8pf4',
            secondary_private_ip_address_count=1
        )
        # 复制代码运行请自行打印 API 的返回值
        await client.create_network_interface_async(create_network_interface_request)


if __name__ == '__main__':
    numbers = 50
    for i in range(numbers):
        Sample.main(sys.argv[1:])
