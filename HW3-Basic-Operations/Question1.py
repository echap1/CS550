'''
CS550 Homework: Basic Operations - Question 1 (Wind Chill)
Due September 13, 2018

@author: Ethan Chapman
'''

import numpy as np
import sys
import os

def main():
    [t, v] = getCmdLineFloats(2)
        
    if np.abs(t) > 50 or v > 120 or v < 3:
        print("Values out of range!\n")
        printHelpStr()
        return
    
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * pow(v, 0.16)
    
    print("Wind Chill: " + str(round(w, 2)) + "°F")
    
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
'''Usage: ''' + getNameStr() + ''' TEMPERATURE WINDSPEED
    
Arguments:
    TEMPERATURE - Temperature (°F)
    WINDSPEED - Wind Speed (mi/h)
    
Notes:
    abs(TEMPERATURE) must be less than or equal to 50
    WINDSPEED must be greater or equal to 3 and less than or equal to 120''')
    
main()