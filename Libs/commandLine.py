"""
Command Line Input Library

@author: Ethan Chapman
"""

import sys
import os


class CommandLine:
    argNames = []
    argTypes = []
    argDescs = []

    file = None
    note = None

    def __init__(self, file):
        self.file = file

    def add_argument(self, name, var_type, desc):
        self.argNames += [name]
        self.argTypes += [var_type]
        self.argDescs += [desc]

    def set_note(self, s):
        self.note = s

        self.note = "    " + self.note
        self.note = self.note.replace("\n", "\n    ")

    def get_arg_values(self):
        arguments = sys.argv
        arguments.pop(0)

        res = []

        if len(arguments) < len(self.argNames):
            self.print_help_str()
            exit()

        try:
            for i in range(len(self.argNames)):
                res += [self.argTypes[i](arguments[i])]
        except:
            print("Invalid Values!\n")
            self.print_help_str()
            exit()

        return res

    def set_program_file(self, f):
        self.file = f

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
