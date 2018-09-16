"""
Basic Command Line Input Library

@author: Ethan Chapman
"""

import sys
import os


class CommandLine:
    argTypes = []

    file = None

    def __init__(self, file):
        self.file = file

    def add_argument(self, var_type):
        self.argTypes += [var_type]

    def get_arg_values(self):
        arguments = sys.argv
        arguments.pop(0)

        res = []

        if len(arguments) < len(self.argTypes):
            print("Not Enough Arguments!")
            exit()

        try:
            for i in range(len(self.argTypes)):
                res += [self.argTypes[i](arguments[i])]
        except:
            print("Invalid Values!")
            exit()

        return res
