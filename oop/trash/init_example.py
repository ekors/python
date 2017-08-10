from oop.trash.lutz import FirstClass

class Init_example(FirstClass):
    def __init__(self, val):
        self.data = val

if __name__ == '__main__':
    a = Init_example(5)
    a.display()