'''
CS550 Classwork: Continuous Interest
September 14, 2018

@author: Ethan Chapman
'''

import numpy as np

import commandLine

def main():
    cl = commandLine.commandLine(__file__)
    
    cl.addArg("P", float, "Principal (Starting Value)")
    cl.addArg("R", float, "Interest Rate")
    cl.addArg("T", float, "Time (y)")
    
    [P, r, t] = cl.getArgValues()
    
    print(round(P * np.exp(r * t)))
    
main()