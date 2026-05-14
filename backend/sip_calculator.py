def calculate_sip(P, annual_rate, years):

    r = annual_rate / 12 / 100
    n = years * 12
    if r == 0:
        FV = P * n
    else:
        FV = P * ((((1 + r) ** n) - 1) / r) * (1 + r)
    invested = P * n
    returns = FV - invested
    FV = round(FV)
    invested = round(invested)
    returns = round(returns)
    return invested, returns, FV