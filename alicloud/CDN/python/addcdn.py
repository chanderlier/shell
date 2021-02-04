import json
from time import sleep
from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest
import AddDomainRecordRequest
from aliyunsdkcdn.request.v20180510.AddCdnDomainRequest
import AddCdnDomainRequest
from aliyunsdkcdn.request.v20180510.DescribeCdnDomainDetailRequest
import DescribeCdnDomainDetailRequest
from aliyunsdkcdn.request.v20180510.SetSourceHostConfigRequest
import SetSourceHostConfigRequest
from aliyunsdkcdn.request.v20180510.DescribeUserDomainsRequest
import DescribeUserDomainsRequest
from aliyunsdkcdn.request.v20180510.DeleteCdnDomainRequest
import DeleteCdnDomainRequest
from aliyunsdkcdn.request.v20180510.DescribeVerifyContentRequest
import DescribeVerifyContentRequest
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def add_domain_cname(client, domain, cname):
    logger.info('add_domain_cname: {}, {}'.format(domain, cname))
    request = AddDomainRecordRequest()
    request.set_accept_format('json')
    request.set_DomainName(domain)
    request.set_RR("file")
    request.set_Type("CNAME")
    request.set_Value(cname)
    response = client.do_action_with_exception(request)
    print(response)


def add_domain_txt(client, domain, records):
    logger.info('add_domain_cname: {}, {}'.format(domain, records))
    request = AddDomainRecordRequest()
    request.set_accept_format('json')
    request.set_DomainName(domain)
    request.set_RR("verification")
    request.set_Type("TXT")
    request.set_Value(records)
    response = client.do_action_with_exception(request)
    print(response)


def add_domain_A(client, domain, records):
    logger.info('add_domain_cname: {}, {}'.format(domain, records))
    request = AddDomainRecordRequest()
    request.set_accept_format('json')
    request.set_DomainName(domain)
    request.set_RR("www")
    request.set_Type("A")
    request.set_Value(records)
    response = client.do_action_with_exception(request)
    print(response)


def add_cdn_domain(client, domain):
    logger.info('add_cdn_domain: {}'.format(domain))
    request = AddCdnDomainRequest()
    request.set_accept_format('json')
    request.set_CdnType("web")
    request.set_DomainName("file." + domain)
    request.set_Sources("[{\"content\":\"1.2.3.4\",\"type\":\"ipaddr\",\"priority\":\"20\",\"port\":80,\"weight\":\"100\"}]")
    response = client.do_action_with_exception(request)
    print(response)


def get_domain_cname(client, domain):
    logger.info('get_domain_cname: {}'.format(domain))
    request = DescribeCdnDomainDetailRequest()
    request.set_accept_format('json')
    request.set_DomainName("file." + domain)
    response = client.do_action_with_exception(request)
    return json.loads(str(response, encoding='utf-8'))['GetDomainDetailModel']['Cname']


def set_source_host_config(client, domain):
    logger.info('set_source_host_config: {}'.format(domain))
    request = SetSourceHostConfigRequest()
    request.set_accept_format('json')
    request.set_DomainName("file." + domain)
    request.set_Enable("on")
    request.set_BackSrcDomain("www.test.cn")
    response = client.do_action_with_exception(request)
    print(response)


def get_offline_domians(client):
    request = DescribeUserDomainsRequest()
    request.set_accept_format('json')
    request.set_PageSize(500)
    request.set_DomainStatus("offline")
    response = client.do_action_with_exception(request)
    # python2:  print(response)
    domains = json.loads(str(response, encoding='utf-8'))['Domains']['PageData']
    return [x['DomainName'] for x in domains]


def delete_cdn_domian(client, domian):
    request = DeleteCdnDomainRequest()
    request.set_accept_format('json')
    request.set_DomainName(domian)
    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))


def verify_domian_owner(client, domian):
    request = DescribeVerifyContentRequest()
    request.set_accept_format('json')
    request.set_DomainName(domian)
    response = client.do_action_with_exception(request)
    verify_str = json.loads(str(response, encoding='utf-8'))['Content']
    print(verify_str)
    add_domain_txt(client, domain, verify_str)


if __name__ == "__main__":
    test_client = AcsClient('', '')
    domains = ['test.cn', 'testing.cn']
    # 添加加速域名， 修改 Host回源设置，添加CNAME解析
    for domain in domains:
        try:
            # add_domain_A(test_client, domain, '5.6.7.8')
            # verify_domian_owner(test_client, domain)
            add_cdn_domain(test_client, domain)
            sleep(5)
            set_source_host_config(test_client, domain)
            sleep(15)
            # 添加 Cname记录单独执行，存在生效时间问题
            cname = get_domain_cname(test_client, domain)
            sleep(3)
            add_domain_cname(test_client, domain, cname)
        except Exception as e:
            logger.error(e)