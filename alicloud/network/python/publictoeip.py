# 将实例的公网IP转化为EIP
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.ConvertNatPublicIpToEipRequest \
    import ConvertNatPublicIpToEipRequest


vhosts = """i-m5ecelicizfkw19lmypn
i-m5ecelicizfkw19lmypo"""

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-qingdao')

request = ConvertNatPublicIpToEipRequest()
request.set_accept_format('json')
for host in vhosts.split('\n'):
    try:
        request.set_InstanceId(host)
        response = client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))
    except Exception as e:
        print('error = ', e)
