# funkcja wyświeta prayste elementy
def print2n(list):  # Versja "klasyczna" modyfikująca wartości listy
    assert (len(list) == 10)
    for i in range(10):
        if list[i] % 2 == 0:
            print(list[i])


# print([0]*5+[2]*4+[7])
print2n([0] * 5 + [2] * 4 + [7])
