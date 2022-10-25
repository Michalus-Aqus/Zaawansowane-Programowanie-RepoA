# funkcja wyświeta na przystych miejscach
def print2i(list):  # Versja "klasyczna" modyfikująca wartości listy
    assert (len(list) == 10)
    for i in range(10):
        if i % 2 == 1:
            print(list[i])


print2i([0] * 5 + [2] * 4 + [7])
