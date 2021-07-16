# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
# 将ecsidlist.txt中的实例和nilist.txt中的辅助弹性网卡绑定
# pip3 install alibabacloud_ecs20140526==2.0.2

import sys
from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
# 将nilist.txt中的内容写入到nilist列表中
with open('nilist.txt', 'r') as f:
    niid = f.readlines()
    nilist = [x.strip() for x in niid if x.strip() != '']
# 将ecsidlist.txt中的内容写入到ecsidlist列表中
with open('ecsidlist.txt', 'r') as f:
    ecsid = f.readlines()
    ecsidlist = [x.strip() for x in ecsid if x.strip() != '']


class AttachNetworkInterfacetoECS:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        config = open_api_models.Config(
            access_key_id='xxx',
            access_key_secret='xxx',
        )
        config.endpoint = 'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = AttachNetworkInterfacetoECS.create_client('accessKeyId', 'accessKeySecret')
        for i in range(len(nilist)):
            attach_network_interface_request = ecs_20140526_models.AttachNetworkInterfaceRequest(
                region_id='cn-shanghai',
                page_size=100,
                instance_id=ecsidlist[i],
                wait_for_network_configuration_ready=False,
                network_interface_id=nilist[i]
            )
            client.attach_network_interface(attach_network_interface_request)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = AttachNetworkInterfacetoECS.create_client('accessKeyId', 'accessKeySecret')
        for i in range(len(nilist)):
            attach_network_interface_request = ecs_20140526_models.AttachNetworkInterfaceRequest(
                region_id='cn-shanghai',
                page_size=100,
                instance_id=ecsidlist[i],
                wait_for_network_configuration_ready=False,
                network_interface_id=nilist[i]
            )
            await client.attach_network_interface_async(attach_network_interface_request)


if __name__ == '__main__':
    AttachNetworkInterfacetoECS.main(sys.argv[1:])
