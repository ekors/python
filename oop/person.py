class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s %s]' % (self.name, self.pay)


class Manager(Person):


    def __init__(self, name, pay):
        super().__init__(name, 'Manager', pay)

    # def __init__(self, name, pay):
    #     Person.__init__(self, name, 'Manager', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
    #     super().giveRaise(percent + bonus)



if __name__ == '__main__':
    bob = Person('Bod Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 1000)
    john = Manager('John Johnes', pay = 2000)
    print(bob)
    print(sue)
    print(john)
    bob.lastName()
    sue.lastName()
    john.lastName()
    sue.giveRaise(0.10)
    john.giveRaise(.10)
    print(sue)
    print(john)

    print('---All three---')
    for o in (bob, sue, john):
        o.giveRaise(.10)
        o.lastName()
        print(o)