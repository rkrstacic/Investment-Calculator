import numpy as np
from scipy.optimize import minimize
from objective import getObjective
from constraints import getCons
from default_values import getRates, getRisk, getYears, getStartingCash, setStartingCash, setYears, setMaxRisk, setRates, setRisk, setMinMaxInv, getMinMaxInv

introStr = """
.  .   .  .  .                       .         
 \  \ /  /   |                      _|_        
  \  \  /.-. | .-..-. .--.--. .-.    |  .-.    
   \/ \/(.-' |(  (   )|  |  |(.-'    | (   )   
    ' '  `--'`-`-'`-' '  '  `-`--'   `-'`-'    
--.--                   .                   .  
  |                    _|_                 _|_ 
  |  .--..    ._.-. .--.|  .--.--. .-. .--. |  
  |  |  | \  / (.-' `--.|  |  |  |(.-' |  | |  
--'--'  `- `'   `--'`--'`-''  '  `-`--''  `-`-'
 .--.     .         .      .                   
:         |         |     _|_                  
|    .-.  | .-..  . | .-.  |  .-. .--.         
:   (   ) |(   |  | |(   ) | (   )|            
 `--'`-'`-`-`-'`--`-`-`-'`-`-'`-' '            
"""

def pre_print():
    print(introStr)
    print()

def getSolution():
    # Guesses as array of zeros
    x0 = np.zeros(len(getRates()))

    return minimize(getObjective, x0, method='SLSQP', constraints=getCons())


def displaySolution():
    for i in range(getYears()):
        sol = getSolution()
        print(f'Year {i + 1}; Best investment with starting cash of {round(getStartingCash(), 2)} is {round(-sol.fun, 2)}')

        for i in range(len(getRates())):
            val = round(sol.x[i], 2)
            print(f"Investment {i + 1}: {abs(val)}")
        
        setStartingCash(round(-sol.fun, 2))
        print()


def inputYears():
    y = int(input("Number of years: "))
    setYears(y)
    print()


def inputStartingCash():
    c = float(input("Starting cash: "))
    setStartingCash(c)
    print()


def inputMinMaxInv():
    userInput = -1
    minMax = []
    setMinMaxInv(minMax)
    while userInput != 0:
        userInput = int(input("Enter min/max constraints.\n0 - Finish\n1 - Min\n2 - Max\n"))

        row = []
        if userInput == 1:
            row.append("min")
        elif userInput == 2:
            row.append("max")

        if userInput != 0:
            userInput = int(input(f"Select investment option ({len(getRates())} available) "))
            row.append(userInput - 1)
        
            userInput = float(input(f"Enter percentage of total investment constraint "))
            row.append(userInput / 100)

        minMax.append(row)

    setMinMaxInv(minMax)
    print()


def inputInv():
    n = int(input("Number of investment options: "))
    setRates([])
    setRisk([])
    for i in range(n):
        # Rate
        rate = float(input(f"Investment option {i + 1} rate: "))
        setRates(getRates() + [rate])

        # Risk
        risk = float(input(f"Investment option {i + 1} risk: "))
        setRisk(getRisk() + [risk])
        print()


def inputMaxRisk():
    r = float(input("Max risk per cash: "))
    setMaxRisk(r)
    print()


def run():
    pre_print()
    
    inputYears()
    inputStartingCash()
    inputInv()
    inputMaxRisk()
    inputMinMaxInv()
    
    displaySolution()
    
    return 0
