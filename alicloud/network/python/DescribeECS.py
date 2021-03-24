# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
# 执行本脚本，将上海区域 ECS InstanceId 写入到ecsidlist.txt中,当前脚本仅支持一百台服务器。
import sys
import ast
from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models


# 清空ecsidlist.txt
def truncatefile():
    with open('ecsidlist.txt', 'w') as f:
        f.truncate()


# 读取文件，将文件中的值写入到data_dict中
def read_file(path):
    with open(path, 'r') as f:
        data = f.read()
        data_dict = ast.literal_eval(data)
    return data_dict


# 提取instance id 写入到ecsidlist.txt中
def parse_data(data_dict):
    data_counts = len(data_dict.get('body').get('Instances').get('Instance'))
    for item in range(data_counts):
        temp_list = []
        ecsid = data_dict.get('body').get('Instances').get('Instance')[item].get('InstanceId')
        temp_list.append(ecsid)
        with open('ecsidlist.txt', 'a') as f:
            f.write('-'.join(temp_list) + '\n')


class DescribeEcsInfo:
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
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
        )
        config.endpoint = 'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id='cn-shanghai',
            page_size=100
        )
        client.describe_instances(describe_instances_request)
        ecs_json = client.describe_instances(describe_instances_request)
        with open('ecsidlist.json', 'w') as f:
            print(ecs_json, file=f)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id='cn-shanghai',
            page_size=100
        )
        await client.describe_instances_async(describe_instances_request)


if __name__ == '__main__':
    DescribeEcsInfo.main(sys.argv[1:])
    truncatefile()
    data_dict = read_file('eceidlist.json')
    parse_data(data_dict)
