from default_values import getStartingCash, getRates, getMinMaxInv, getRisk, getMaxRisk
from numpy import dot

def getCons():
    # Invested amount must be smaller or equal to starting cash
    def investConstraint(x):
        return getStartingCash() - sum(x)
        
    def riskConstraint(x):
        return getMaxRisk() - dot(getRisk(), x) / getStartingCash()


    cons = [
        { 'type': 'ineq', 'fun': investConstraint },
        { 'type': 'ineq', 'fun': riskConstraint },
    ]

    # Helper function for early binding
    def factory0(i):
        return (lambda x: x[i])

    # Adding non negative constrains    
    for i in range(len(getRates())):
        cons.append(
            { 'type': 'ineq', 'fun': factory0(i) }
        )

    # Helper function for early binding
    def factory(i, p, key):
        if key == "min":
            return (lambda x: x[i] / getStartingCash() - p)
        elif key == "max":
            return (lambda x: p - x[i] / getStartingCash())
        
        return None

    # Adding min/max Investment constrains
    for item in getMinMaxInv():
        if len(item) == 0:
            break
            
        key, inv, p = item
        fun = factory(inv, p, key)
        
        cons.append(
            { 'type': 'ineq', 'fun': fun }
        )

    return cons
