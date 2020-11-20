from abc import ABCMeta,abstractmethod

class Employee(object,metaclass=ABCMeta):
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    def __init__(self,name,working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self,working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour

class Salesman(Employee):

    def __init__(self,name,sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main():
    emps = [Manager('Dieser'),Programmer('Refrain'),Manager('Kate Sun'),Salesman('Fisher'),Programmer('Lieber')]
    for emp in emps:
        if isinstance(emp,Programmer):
            emp.working_hour = int(input('please input %s working hours this month:' % emp.name))
        elif isinstance(emp,Salesman):
            emp.sales = float(input('please input %s sales money this month: ' % emp.name))
        print('%s salary this month is:￥%s' % (emp.name,emp.get_salary()))

if __name__ == '__main__':
    main()

