"""
CS550 Homework: Basic Operations - Question 3 (Day of Week)
Due September 14, 2018

@author: Ethan Chapman
"""

import commandLine

def main():
    cl = commandLine.commandLine(__file__)
    
    cl.addArg("MONTH", float, "A number representing the month (ex. 1 for January, 2 for Febuary)")
    cl.addArg("DAY", float, "The day of the year")
    cl.addArg("YEAR", float, "The year")
    
    [m, d, y] = cl.getArgValues()
    
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31 * m0) // 12) % 7
    d0 = int(d0)
    
    print(days[d0])
    
main()