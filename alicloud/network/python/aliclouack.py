# -*- coding: utf-8 -*-
# pip3 install alibabacloud_ecs20140526==2.0.2
# 创建阿里云登录类,ack连接函数
from alibabacloud_vpc20160428.client import Client as Vpc20160428Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_vpc20160428 import models as vpc_20160428_models


class logininfo:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Vpc20160428Client:
        config = open_api_models.Config(
            access_key_id='xxxx',
            access_key_secret='xxxx',
        )
        config.endpoint = 'vpc.aliyuncs.com'
        return Vpc20160428Client(config)
