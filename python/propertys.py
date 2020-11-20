class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age  = age


        @property
        def name(self):
            return self._name


        @propert
        def age(self):
            return self._age

        @age.setter
        def age(self,age):
            self._age = age


        def play(self):
            if self._age <= 16:
                print('%s is playing chess.' % self._name)
            else:
                print('%s is playing poke.' % self._name)


def main():
    person = Person('refrain',14)
    person.play()
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()
