def is_even(num: int):
    return num % 2 == 0


even = is_even(17)
print("Liczba parzysta" if even else "Liczba nie parzysta")
