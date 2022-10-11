#funkcja otrzymuje listę 5 imion i wyświetla każde z nich
def print_names(five_names):
    assert(len(five_names)==5)
    for id in range(5):
        print(five_names[id])

print_names(["Alan","Bob","John","James","Mark"])
