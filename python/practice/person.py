class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    
    def __str__(self):
        return '[Person: %s,%s]' % (self.name, self.pay)


if __name__ == "__main__":
    Bob = Person('Bob Smith')
    Sue = Person('Sue Jones', job='dev', pay=10000)
    print(Bob.name, Bob.pay)
    print(Sue.name, Sue.pay)
    print(Bob.lastname(), Sue.lastname())
    Sue.giveRaise(.10)
    print(Sue.pay)
    print(Sue)