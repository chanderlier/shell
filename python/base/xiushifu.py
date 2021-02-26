def funA(fn):
    print('A')
    fn()
    return 'fkit'


@funA

def funB():
    print('B')
print(funB)


def decorator(func):
    def wrapper():
        print('Decorated function')
    print('123')
    return wrapper


@decorator

def test():
    print('Test')


test()
print("funcname: %s" % test.__name__)