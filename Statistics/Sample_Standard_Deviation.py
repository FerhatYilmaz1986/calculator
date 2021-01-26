from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Statistics.Getsample import getSample
from Calculator.Squareroot import squareroot
from Calculator.Square import square
from Statistics.SampleMean import sample_mean
from Calculator.Addition import addition


def sample_st_deviation(data, sample_size):
    dev = 0
    sample = getSample(data, sample_size)
    sample_values = len(sample)
    x_bar = sample_mean()
    x = sample_values
    n = subtraction(sample_values, 1)
    for dev in sample:
        dev = subtraction(x, x_bar)
        square_x_bar = square(dev)
        add = addition(square_x_bar, square_x_bar)
        divide = division(add, n)
    return squareroot(divide)
