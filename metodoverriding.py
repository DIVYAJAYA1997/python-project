class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name
obj=Parent("ATHULYA",23)
print(obj)