import sys
import json
import requests


# API 地址
domain_list_url = 'https://dnsapi.cn/Domain.List'
record_list_url = 'https://dnsapi.cn/Record.List'
record_create_url = 'https://dnsapi.cn/Record.Create'


def get_domian_id(domain):
    body = {
        "login_token": api_token,
        "type": "all",
        "keyword": domain
    }
    res = requests.post(domain_list_url, data=body)
    try:
        domains = json.loads(res.text)['domains']
        for item in domains:
            if domain == item['name']:
                return item['id']
    except Exception as e:
        print(e)
        return None


def add_domain_record(domain, sub, slb_ip):
    if is_exist_sub_domain(domain, sub):
        print("The Record [ {} ] is alrealdy exist".format(sub))
    else:
        domian_id = get_domian_id(domain)
        body = {
            "login_token": api_token,
            "domian_id": domian_id,
            "sub_domain": sub,
            "record_type": "A",
            "value": slb_ip,
            "record_line": "默认",
            "domain": domain
        }
        res = requests.post(record_create_url, data=body)
        res_code = json.loads(res.text)['status']['code']
        if res_code == '1':
            print("The Record [ {} ] is add success".format(sub))
            return True
        else:
            print("The Record [ {} ] is add failed".format(res.text))
            print(res.text)
            return True


def is_exist_sub_domain(domain, sub):
    body = {
        "login_token": api_token,
        "domain": domain,
        "sub_domain": sub
    }
    res = requests.post(record_list_url, data=body)

    stat_code = json.loads(res.text)['status']['code']
    if stat_code == '10':
        print("The Record [ {} ] is not exist".format(sub))
        return None
    else:
        print(json.loads(res.text))
        return True


if __name__ == "__main__":
    full_domain = sys.argv[1]
    sub = full_domain.split('.')[0]
    domain = '.'.join(full_domain.split('.')[1:])
    if domain == 'dieser.com':
        api_token = 'id,key'
        slb_ip = '1.2.3.4'
        add_domain_record(domain, sub, slb_ip)
    elif domain == 'dieser.cn':
        api_token = 'id,key'
        slb_ip = '2.3.4.5'
        add_domain_record(domain, sub, slb_ip)
    elif domain == 'dieser.cc':
        api_token = 'id,key'
        slb_ip = '4.5.6.7'
        add_domain_record(domain, sub, slb_ip)
    else:
        print("The domain {} is not support".format(full_domain))
