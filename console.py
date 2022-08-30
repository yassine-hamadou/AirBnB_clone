#!/usr/bin/env python3
"""AirBnB command interpreter"""
import cmd
class AirBnBShell(cmd.Cmd):
    """Command processor for our AirBnB Project."""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """End of File"""
        return True

if __name__ == '__main__':
    AirBnBShell().cmdloop()
