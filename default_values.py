rates = [0.0002, 0.0002, 0.016, 2.85, 19.92, 1.06, 0.31, 0.016, 0.0003, 0.0003]
risk = [2, 3, 15, 150, 200, 50, 80, 15, 2, 3]
startingCash = 150_000
maxRisk = 10
years = 10
minMaxInv = [
    ["min", 2, 0.125],
    ["min", 3, 0.01],
    ["min", 4, 0.01],
    ["min", 5, 0.01],
    ["min", 6, 0.01],
    ["min", 7, 0.125],
    
    ["max", 3, 0.1],
    ["max", 4, 0.1],
    ["max", 5, 0.1],
    ["max", 6, 0.1],
]

def getRates():
    return rates

def getRisk():
    return risk

def getStartingCash():
    return startingCash

def getMinMaxInv():
    return minMaxInv

def getMaxRisk():
    return maxRisk

def getYears():
    return years


def setRates(x):
    global rates
    rates = x

def setRisk(x):
    global risk
    risk = x

def setStartingCash(x):
    global startingCash
    startingCash = x

def setMinMaxInv(x):
    global minMaxInv
    minMaxInv = x

def setMaxRisk(x):
    global maxRisk
    maxRisk = x

def setYears(x):
    global years
    years = x
