'''
CS550 Homework: Basic Operations - Question 1
Due September 13, 2018

@author: Ethan Chapman
'''

import sys
import os

def main():
    [x, y, z] = getCmdLineFloats(3)
    
    if x < y < z or x > y > z:
        print(True)
        
    else:
        print(False)

def getCmdLineFloats(n):
    arguments = sys.argv
    arguments.pop(0)
    
    res = []
    
    if len(arguments) < n:
        printHelpStr()
        exit()
    
    try:
        for i in range(n):
            res += [float(arguments[i])]
    except:
        print("Invalid Values!\n")
        printHelpStr()
        exit()
        
    return res
    
def getNameStr():
    return "python3 " + os.path.basename(os.path.realpath(__file__))
    
def printHelpStr():
    print(
'''Usage: ''' + getNameStr() + ''' X Y Z
    
Arguments:
    X, Y, Z - 3 floating point numbers''')
    
main()