#!/usr/bin/env python3
"""AirBnB command interpreter"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel

classes = [
    "BaseModel"
]


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Command processor for our AirBnB Project."""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """End of File"""
        return True

    def emptyline(self):
        """Execute nothing """
        pass
    
    def do_create(self, args):
        """ Creates a new instance """
        if not (args):
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval[args]()
            instance.save()
            print(instance.id)

            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
