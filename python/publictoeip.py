i-m5ecelicizfkw19lmypn
i-m5ecelicizfkw19lmypo
i-m5ecelicizfkw19lmypp
i-m5ecelicizfkw19lmypq
i-m5ecelicizfkw19lmypr
i-m5ecelicizfkw19lmyps
i-m5ecelicizfkw19lmypt
i-m5ecelicizfkw19lmypu
i-m5ecelicizfkw19lmypv
i-m5ecelicizfkw19lmypw
i-m5ecelicizfkw19lmypx
i-m5ecelicizfkw19lmypz
i-m5ecelicizfkw19lmyq0
i-m5ecelicizfkw19lmyq1
i-m5ecelicizfkw19lmyq2
i-m5ecelicizfkw19lmyq3
i-m5ecelicizfkw19lmyq4
i-m5ecelicizfkw19lmyq5
i-m5ecelicizfkw19lmyq6
i-m5ecelicizfkw19lmyq7
i-m5ecelicizfkw19lmyq8
i-m5ecelicizfkw19lmyq9
i-m5ecelicizfkw19lmyqa
i-m5ecelicizfkw19lmyqb
i-m5ecelicizfkw19lmyqc
i-m5ecelicizfkw19lmyqd
i-m5ecelicizfkw19lmyqe
i-m5ecelicizfkw19lmyqf
i-m5ecelicizfkw19lmyqg
i-m5ecelicizfkw19lmyqh
i-m5ecelicizfkw19lmyqi
i-m5ecelicizfkw19lmyqj
i-m5ecelicizfkw19lmyqk
i-m5ecelicizfkw19lmyql
i-m5ecelicizfkw19lmyqm
i-m5ecelicizfkw19lmyqn
i-m5ecelicizfkw19lmyqo
i-m5ecelicizfkw19lmyqp
i-m5ecelicizfkw19lmyqq
i-m5ecelicizfkw19lmyqr
i-m5ecelicizfkw19lmyqs
i-m5ecelicizfkw19lmyqt
i-m5ecelicizfkw19lmyqu
i-m5ecelicizfkw19lmyqv
i-m5ecelicizfkw19lmyqw
i-m5ecelicizfkw19lmyqx
i-m5ecelicizfkw19lmyqy
i-m5ecelicizfkw19lmyqz
i-m5ecelicizfkw19lmyr0
i-m5ecelicizfkw19lmyr1
i-m5ecelicizfkw19lmyr2
i-m5ecelicizfkw19lmyr3
i-m5ecelicizfkw19lmyr4
i-m5ecelicizfkw19lmyr5
i-m5ecelicizfkw19lmyr6
i-m5ecelicizfkw19lmyr7
i-m5ecelicizfkw19lmyr8
i-m5ecelicizfkw19lmyr9
i-m5ecelicizfkw19lmyra
i-m5ecelicizfkw19lmyrb
i-m5ecelicizfkw19lmyrc
i-m5ecelicizfkw19lmyrd
i-m5ecelicizfkw19lmyre
i-m5ecelicizfkw19lmyrf
i-m5ecelicizfkw19lmyrg
i-m5ecelicizfkw19lmyrh
i-m5ecelicizfkw19lmyri
i-m5ecelicizfkw19lmyrj
i-m5ecelicizfkw19lmyrk
i-m5ecelicizfkw19lmyrl
i-m5ecelicizfkw19lmyrm
i-m5ecelicizfkw19lmyrn
i-m5ecelicizfkw19lmyro
i-m5ecelicizfkw19lmyrp
i-m5ecelicizfkw19lmyrq
i-m5ecelicizfkw19lmyrr
i-m5ecelicizfkw19lmyrs
i-m5ecelicizfkw19lmyrt
i-m5ecelicizfkw19lmyru
i-m5ecelicizfkw19lmyrv
i-m5ecelicizfkw19lmyrw
i-m5ecelicizfkw19lmyrx
i-m5ecelicizfkw19lmyry
i-m5ecelicizfkw19lmyrz
i-m5ecelicizfkw19lmys0
i-m5ecelicizfkw19lmys1
i-m5ecelicizfkw19lmys2
i-m5ecelicizfkw19lmys3
i-m5ecelicizfkw19lmys4
i-m5ecelicizfkw19lmys6
i-m5ecelicizfkw19lmys7
i-m5ecelicizfkw19lmys8
i-m5ecelicizfkw19lmys9
i-m5ecelicizfkw19lmysa
i-m5ecelicizfkw19lmysb
i-m5ecelicizfkw19lmysc
i-m5ecelicizfkw19lmysd






#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.ConvertNatPublicIpToEipRequest import ConvertNatPublicIpToEipRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-qingdao')

request = ConvertNatPublicIpToEipRequest()
request.set_accept_format('json')

request.set_InstanceId("i-m5ecelicizfkw19lmypm")

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))