#funkcja mnożąca elementy lity przez 2
def mul2(list):#Versja "klasyczna" modyfikująca wartości listy
    for id in range(len(list)):
        list[id]*=2
    return list

def mul2B(list):
    return [2*x for x in list]

print(mul2([1,7,10]))
print(mul2B([1,7,10]))