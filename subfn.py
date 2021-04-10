def sub_sm(fun):
    def inner(a,b):
        if a<b :
            (a,b)=(b,a)
            return (sub(a,b))
        return fun(a,b)
    return inner
@sub_sm
def sub(a,b):
    return a-b
print(sub(100,200))
