"""
Command Line Input Library

@author: Ethan Chapman
"""

import sys

from typing import *

from commandLine import Argument


class BasicCommandLine:
    @staticmethod
    def get_arg_values(arg_types: List[Argument]):
        arguments = sys.argv
        arguments.pop(0)

        res: List[str] = []

        if len(arguments) < len(arg_types):
            print("Not Enough Inputs!")
            exit()

        try:
            for i in range(len(arg_types)):
                res += [arg_types[i].get_type()(arguments[i])]

                if not arg_types[i].get_validity_function()(res[len(res) - 1]):
                    print("Values Not In Range!")
                    exit()


        except ValueError:
            print("Invalid Values!")
            exit()

        return res
