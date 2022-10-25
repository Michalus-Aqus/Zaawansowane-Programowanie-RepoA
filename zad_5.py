def is_in(l: list, n: int):
    return n in l


print(is_in([1, 2, 3], 4))
print(is_in([1, 2, 3], 3))

"""
def has_someting_in_common(a:list,b:list):
    return any([ea == eb or (is_nan(ea) and is_nan(eb)) for ea in a for eb in b])

def is_nan(x):
    return str(type(float("nan")).__name__)=='float' and x!=x


print(has_someting_in_common([1,2,3],["1",0,-1]))
print(has_someting_in_common([1,2,3],[1,0,-1]))
print(has_someting_in_common([[],2,3],[[],0,-1]))
print(has_someting_in_common([[],2,3],[[],0,-1]))
print(has_someting_in_common([float("nan"),2,3],[float("nan"),0,-1]))

"""
