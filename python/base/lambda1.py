principal = 1000
rate = 0.05
payment = 80
month = 0
res = []
while principal > 0:
    month += 1
    principal = principal * (1 + rate/12) - payment
    res.append(principal)


print(res[-2])
"""
res = []
month = 0
principal = 1000
rate = 0.05
payment = 80
"""
"""
def principalindex(n):
    res = []
    month = 0
    principal = 1000
    rate = 0.05
    payment = 80
    while principal > 0:
        month = month + 1
        principal = principal - payment
        res.append(principal)
        return res

print(principalindex(10))
"""





"""
def f1():
    x = 99
    def f2():
        def f3():
            print(x)
        f3()
        f2()


f1()
"""
"""
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested


F = tester(10543)
F('spam')
F('abc')
"""

"""
class tester:
    def __init__(self, start):
        self.state = start

    def nested(self, label):
        print(label, self.state)
        self.state += 1


F = tester(0)
F.nested('spam')
"""
"""
def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res


def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]


print(min1(3, 4, 1, 2))
print(min2("bb", "aa"))
print(min3([2, 2], [1, 1], [3, 3], [1, 4]))
"""