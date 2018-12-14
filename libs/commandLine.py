"""
Command Line Input Library

@author: Ethan Chapman
"""

import sys
import os
import subprocess

from typing import List

class Argument:
    argType: type = None
    validityFunction = None

    def __init__(self, arg_type: type, validity_function=lambda x: True):
        self.argType = arg_type
        self.validityFunction = validity_function

    def get_type(self):
        return self.argType

    def get_validity_function(self):
        return self.validityFunction


class VarInput(object):
    def __init__(self, invalid_handler=None):
        if invalid_handler is not None: self.invalidHandler = invalid_handler
        else: self.invalidHandler = self.__default_handler

    def input(self, message: str, argument: Argument):
        input_str = input(message)

        try:
            input_val = argument.get_type()(input_str)

        except ValueError:
            return self.invalidHandler(input_str, [message, argument], True)

        if not argument.get_validity_function()(input_val):
            return self.invalidHandler(input_str, [message, argument], False)

        return input_val

    def __default_handler(self, value, params, value_error):
        print("Value Invalid!")
        return self.input(*params)


class CommandLine:
    argNames: List[str] = []
    argTypes: List[Argument] = []
    argDescs: List[str] = []

    file = None
    note = None

    def __init__(self, file):
        self.file = file

    def add_argument(self, name: str, var_type: Argument, desc: str):
        self.argNames += [name]
        self.argTypes += [var_type]
        self.argDescs += [desc]

    def set_note(self, s: str):
        self.note = s

        self.note = "    " + self.note
        self.note = self.note.replace("\n", "\n    ")

    def get_arg_values(self):
        arguments = sys.argv
        arguments.pop(0)

        res: list = []

        if len(arguments) < len(self.argNames):
            if len(arguments) == 0:
                var_in = VarInput()

                for i in range(len(self.argTypes)):
                    res += [var_in.input(self.argNames[i] + ": ", self.argTypes[i])]

                return res
            else:
                self.print_help_str()
                exit()

        try:
            for i in range(len(self.argNames)):
                res += [self.argTypes[i].get_type()(arguments[i])]

                if not self.argTypes[i].get_validity_function()(res[len(res) - 1]):
                    print("Values Not In Range!\n")
                    self.print_help_str()
                    exit()


        except ValueError:
            print("Invalid Values!\n")
            self.print_help_str()
            exit()

        return res

    def get_name_str(self):
        return "python3 " + os.path.basename(os.path.realpath(self.file))

    def print_help_str(self):
        arg_str = " "
        arg_help_str = ""

        for i in range(len(self.argNames)):
            arg_str += self.argNames[i] + " "
            arg_help_str += "\n    " + self.argNames[i] + " - " + self.argDescs[i]

        print("Usage: " + self.get_name_str() + arg_str)
        print("\nArguments:" + arg_help_str)

        if self.note is not None:
            print("\nNotes:")
            print(self.note)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def open(filepath):
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', filepath))

    elif os.name == 'nt':  # For Windows
        os.startfile(filepath)

    elif os.name == 'posix':  # For Linux, Mac, etc.
        subprocess.call(('xdg-open', filepath))