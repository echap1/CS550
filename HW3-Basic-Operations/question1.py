"""
CS550 Homework: Basic Operations - Question 1 (Wind Chill)
Due September 14, 2018

@author: Ethan Chapman
"""

import sys
sys.path.append("..")

from libs.commandLine import *

import numpy as np


def main():
    cl = CommandLine(__file__)

    cl.add_argument("TEMPERATURE", Argument(float, lambda x: np.abs(x) <= 50), "Temperature (°F)")
    cl.add_argument("WINDSPEED", Argument(float, lambda x: 3 <= x <= 120), "Wind Speed (mi/h)")

    cl.set_note("abs(TEMPERATURE) must be less than or equal to 50\n" +
                "WINDSPEED must be greater or equal to 3 and less than or equal to 120")

    [t, v] = cl.get_arg_values()

    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * pow(v, 0.16)

    print("Wind Chill: " + str(round(w, 2)) + "°F")


main()
