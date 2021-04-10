class Person:
    def self_values(self,age,name):
        self.age=age
        self.name=name
    def print_values(self):

        print(self.name)
        print(self.age)

obj=Person()
obj.self_values(23,"ARATHI")
obj.print_values()