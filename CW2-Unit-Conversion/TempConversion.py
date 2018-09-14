'''
CS550 Classwork: Unit Conversion
September 10, 2018

@author: Ethan Chapman
'''

def main():
    units = "CFK"
    
    inputType = input("Input inputType (C, F, or K): ")
    
    if not(inputType in "CFK" and len(inputType) == 1):
        print("Invalid Input")
        exit()
    
    toCelsius = {"C": lambda c: c, "F": lambda f: (f - 32) * 1.8, "K": lambda k: k - 273.15}
    fromCelsius = {"C": lambda c: c, "F": lambda c: c * 1.8 + 32, "K": lambda c: c + 273.15}
    
    inputVal = "i"
    
    try:
        inputVal = float(input("Temp (" + inputType + "): "))
    finally:
        if inputVal == "i":
            print("Invalid Input")
            exit()

    print()
    
    celcius = toCelsius[inputType](inputVal)
    
    for i in range(len(units)):
        c = units[i]
        
        print("Temp in " + c + ": " + str(fromCelsius[c](celcius)))
    
main()