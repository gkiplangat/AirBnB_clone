#!/usr/bin/env python3

""" Command line interpreter for AirBnB """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """
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

    def do_create(self, arg):
        """ Creates new instance of Basemodel, 
            saves it into JSON file
            and prints its id.
        """
        if not arg:
            print("** class name missing **")
            return
        
        class_name = arg
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
