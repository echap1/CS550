'''
CS550 Homework: Basic Operations - Question 1
Due September 13, 2018

@author: Ethan Chapman
'''

import sys
import os

def main():
    [m, d, y] = getCmdLineFloats(3)
    
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31 * m0) // 12) % 7
    d0 = int(d0)
    
    print(days[d0])
    
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
'''Usage: ''' + getNameStr() + ''' MONTH DAY YEAR
    
Arguments:
    MONTH - A number representing the month (ex. 1 for January, 2 for Febuary)
    DAY - The day of the month
    YEAR - The year
    
Notes:
    abs(TEMPERATURE) must be less than or equal to 50
    WINDSPEED must be greater or equal to 3 and less than or equal to 120''')
    
main()