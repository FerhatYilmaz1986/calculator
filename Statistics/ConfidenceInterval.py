from Statistics.SampleMean import sample_mean
from Statistics.PopulationStandardDeviation import pop_standard_dev
from Calculator.Division import division
from Calculator.Squareroot import squareroot
from Calculator.Multiplication import multiplication
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition


def confidence_interval(data):
    z_value = 1.05
    mean =sample_mean(data)
    sd = pop_standard_dev(data)
    x = len(data)
    y = division(squareroot(x), sd)
    margin_of_error = multiplication(z_value, y)
    a = subtraction(mean, margin_of_error)
    b = addition(mean, margin_of_error)
    return a, b
