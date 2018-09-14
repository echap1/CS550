'''
Command Line Input Library

@author: Ethan Chapman
'''

import sys
import os

class commandLine:
    argNames = []
    argTypes = []
    argDescs = []
    
    file = None
    note = None
    
    def __init__(self, file):
        self.file = file
        
    def addArg(self, name, type, desc):
        self.argNames += [name]
        self.argTypes += [type]
        self.argDescs += [desc]
    
    def setNoteStr(self, s):
        self.note = s
    
        self.note = "    " + self.note
        self.note = self.note.replace("\n", "\n    ")
        
    def getArgValues(self):
        arguments = sys.argv
        arguments.pop(0)
        
        res = []
        
        if len(arguments) < len(self.argNames):
            self.printHelpStr()
            exit()
        
        try:
            for i in range(len(self.argNames)):
                res += [self.argTypes[i](arguments[i])]
        except:
            print("Invalid Values!\n")
            self.printHelpStr()
            exit()
            
        return res
        
    def setProgramFile(self, f):
        global file
        
        file = f
        
    def getNameStr(self):
        return "python3 " + os.path.basename(os.path.realpath(self.file))
    
    def printHelpStr(self):
        argStr = " "
        argHelpStr = ""
        
        for i in range(len(self.argNames)):
            argStr += self.argNames[i] + " "
            argHelpStr += "\n    " + self.argNames[i] + " - " + self.argDescs[i]
        
        print("Usage: " + self.getNameStr() + argStr)
        print("\nArguments:" + argHelpStr)
        
        if self.note != None:
            print("\nNotes:")
            print(self.note)
        