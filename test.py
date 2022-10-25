#funkcja liczy nany
def count_nans(ar:list):
    return sum([type(1.0).__name__=='float' and e!=e for e in ar])


print(count_nans([float('nan'),float('1'),float('nan'),float('2')]))

