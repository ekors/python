class FirstClass:
    def setData(self, value):
        self.data = value
    def display(self):
        print(self.data)






if __name__ == "__main__":
    x = FirstClass()
    y = FirstClass()
    x.setData(2)
    y.setData("two")
    x.display()
    y.display()