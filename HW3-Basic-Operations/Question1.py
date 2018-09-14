"""
CS550 Homework: Basic Operations - Question 1 (Wind Chill)
Due September 14, 2018

@author: Ethan Chapman
"""

import numpy as np

import commandLine

def main():
    cl = commandLine.commandLine(__file__)
    
    cl.addArg("TEMPERATURE", float, "Temperature (°F)")
    cl.addArg("WINDSPEED", float, "Wind Speed (mi/h)")
    
    cl.setNoteStr("abs(TEMPERATURE) must be less than or equal to 50\n"+
                           "WINDSPEED must be greater or equal to 3 and less than or equal to 120")
    
    [t, v] = cl.getArgValues()
        
    if np.abs(t) > 50 or v > 120 or v < 3:
        print("Values out of range!\n")
        cl.printHelpStr()
        return
    
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * pow(v, 0.16)
    
    print("Wind Chill: " + str(round(w, 2)) + "°F")
    
main()