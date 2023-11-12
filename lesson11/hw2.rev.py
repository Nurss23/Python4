def bank(contr, year):
    res = contr * 0.10 * year + contr
    return res

contr = 300
year = 5
sym = bank(contr, year)
print(round(sym, 2))