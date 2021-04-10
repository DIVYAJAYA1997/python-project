class A:
    def func(self):
        print("CLASS A")
class B:
    def func(self):
        print("CLASS B")

class C:
    def start(self,sd):
        sd.func()
obj=A()
obj1=C()
obj1.start(obj)
