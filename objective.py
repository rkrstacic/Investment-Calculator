from numpy import dot
from default_values import getRates

def getMultRates(r):
    return list(map(lambda x: x + 1, r))

def getInvested(x):
    return dot(getMultRates(getRates()), x)

def getObjective(x):
    return -getInvested(x)
