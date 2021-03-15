class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

x.setdata('Dieser')
y.setdata(3.23422323)

x.display()
y.display()

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def into(self):
        return (self.name, self.job)


rec1 = Person('mel', 'trainer')
rec2 = Person('vls', 'developer')

print(rec1.job)