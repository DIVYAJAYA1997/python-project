
def samrt_div(fun):
    def inner(no1,no2):
        if no1<no2:
            (no1,no2)=(no2,no1)
        return fun(no1,no2)
    return inner
@samrt_div
def sub(no1,no2):
    return no1-no2
print(sub(10,20))