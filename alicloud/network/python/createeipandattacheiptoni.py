# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models


class createeip:
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
        client = createeip.create_client('accessKeyId', 'accessKeySecret')
        allocate_eip_address_request = ecs_20140526_models.AllocateEipAddressRequest(
            region_id='cn-qingdao'
        )
        for i in range(150):
            try:
                client.allocate_eip_address(allocate_eip_address_request)
            except (RuntimeError, TypeError, NameError):
                pass
            except Exception:
                print("Unexpected error:", sys.exc_info()[0])
                raise

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = createeip.create_client('accessKeyId', 'accessKeySecret')
        allocate_eip_address_request = ecs_20140526_models.AllocateEipAddressRequest(
            region_id='cn-qingdao'
        )
        await client.allocate_eip_address_async(allocate_eip_address_request)


if __name__ == '__main__':
    createeip.main(sys.argv[1:])
