class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def study(self,course_name):
        print('%s is studying %s.' %(self.name,course_name))
    
    def watch_movie(self):
        if self.age < 18:
            print('%s can only watch acg.' % self.name)
        else:
            print('%s is watching r18.' % self.name)



def main():
    stu1 = Student('refrain',27)
    stu1.study('python program design')
    stu1.watch_movie()
    stu2 = Student('dieser',14)
    stu2.study('go program design')
    stu2.watch_movie()

if __name__ == '__main__':
    main()
