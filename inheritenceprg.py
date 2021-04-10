class Parent:
    def print_data(self):
        print("INSIDE PARENT")

class Child():
    def print_data(self):
        print("inside CHILD")
class Subchild(Child,Parent):
    def demo(self):
        print("INSIDE SUBCHILD")


obj1=Subchild()
obj1.demo()
obj1.print_data()
objec=Child()
objec.print_data()