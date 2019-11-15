from Statistics.PopulationMean import population_mean
from Calculator.Squareroot import squareroot


def pop_standard_dev(data):
    n = len(data)
    u = population_mean(data)
    return squareroot(sum([(element - u) ** 2 for element in data]) / (len(data) - 1))