from Calculator.Addition import addition
from Calculator.Division import division


def proportion(data):
    p = len(data)
    age = 0
    for values in data:
        if age > 62:
            addition(age)
    return division(values, p)
