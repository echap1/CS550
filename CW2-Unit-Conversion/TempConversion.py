"""
CS550 Classwork: Unit Conversion
September 10, 2018

@author: Ethan Chapman
"""


def main():
    units = "CFK"

    input_type = input("Input (C, F, or K): ")

    if not (input_type in "CFK" and len(input_type) == 1):
        print("Invalid Input")
        exit()

    to_celsius = {"C": lambda c: c, "F": lambda f: (f - 32) * 1.8, "K": lambda k: k - 273.15}
    from_celsius = {"C": lambda c: c, "F": lambda c: c * 1.8 + 32, "K": lambda c: c + 273.15}

    input_val = "i"

    try:
        input_val = float(input("Temp (" + input_type + "): "))
    finally:
        if input_val == "i":
            print("Invalid Input")
            exit()

    print()

    celsius = to_celsius[input_type](input_val)

    for i in range(len(units)):
        c = units[i]

        print("Temp in " + c + ": " + str(from_celsius[c](celsius)))


main()
