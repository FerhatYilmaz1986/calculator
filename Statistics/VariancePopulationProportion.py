from Statistics.Proportion import proportion
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Multiplication import multiplication


def variance_pop_proportion(data):
    p = proportion(data)
    s = subtraction(p, 1)
    n = len(data)
    return division(multiplication(p, s), n)
