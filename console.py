#!/usr/bin/env python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program by pressing Ctrl+D"""
        return True
    
    def help_quit(self):
        """Help guide for quit command"""
        print('Quit command to exit the program')

    def help_EOF(self):
        """Help guide for EOF command"""
        print('EOF command to exit the program')

    def emptyline(self):
        """Handles empty lines"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
