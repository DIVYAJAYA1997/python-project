class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __sub__(self, other):
        return Book(self.pages-other.pages)
    def __str__(self):
        return str(self.pages)

obj=Book(100)
obj1=Book(300)
obj2=Book(200)
print(obj1-obj2-obj)
print(obj+obj1+obj2)