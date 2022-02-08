import redis


def connect(ip, port, db, passwd):
    r = redis.Redis(host=ip, port=port, db=db, password=passwd)
    a = r.dbsize()
    b = r.keys('91ip*')
    print(b)


if __name__ == "__main__":
    connect('10.0.3.110', '6379', '22', 'xxxxz')
