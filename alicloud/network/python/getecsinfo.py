#!/usr/bin/python3
from alicloudack import logininfo
import sys
import os
import json
import ast
import requests
from typing import List
from alibabacloud_vpc20160428.client import Client as Vpc20160428Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_vpc20160428 import models as vpc_20160428_models


class getinfo():
    def __init__():
        pass

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = logininfo.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='ap-southeast-1',
            page_size=50,
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
        client = logininfo.create_client('accessKeyId', 'accessKeySecret')
        describe_eip_addresses_request = vpc_20160428_models.DescribeEipAddressesRequest(
            region_id='ap-southeast-1',
            page_size=50,
            page_number=1
        )
        await client.describe_eip_addresses_async(describe_eip_addresses_request)


if __name__ == '__main__':
    getinfo.main(sys.argv[1:])
