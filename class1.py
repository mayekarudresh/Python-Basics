# oops concepts: 1. class it is the unit of the program which have member variable and member methods
# using object can access class properties ...


class Person:
    def get(self):
        self.a=34
        self.b=45

    def display(self):
        print("result=",self.a+self.b)


p=Person()
p.get()
p.display()


p1=Person()
p1.get()
p1.display()
