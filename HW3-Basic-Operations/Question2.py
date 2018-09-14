'''
CS550 Homework: Basic Operations - Question 2 (XYZ)
Due September 14, 2018

@author: Ethan Chapman
'''

import commandLine

def main():
    cl = commandLine.commandLine(__file__)
    
    cl.addArg("X", float, "First Number")
    cl.addArg("Y", float, "Second Number")
    cl.addArg("Z", float, "Third Number")
    
    [x, y, z] = cl.getArgValues()
    
    print(x < y < z or x > y > z)
    
main()