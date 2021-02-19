def f1():
    x = 99
    def f2():
        def f3():
            print(x)
        f3()
        f2()


f1()
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


class tester:
    def __init__(self, start):
        self.state = start
    def nested(self, label):
        print(label, self.state)
        self.state += 1 

F = tester(0)
F.nested('spam')