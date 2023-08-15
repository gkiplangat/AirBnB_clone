#!/usr/bin/python3

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
        """ 
            Task: 7. Console 0.1
            Creates new instance of Basemodel, 
            saves it into JSON file
            and prints its id.
        """
        if not arg:
            print("** class name missing **")
            return
        
        class_name = arg
        if class_name not in storage.all_classes:
            print("** class doesn't exist **")
            return
        
        new_instance = storage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)

def do_show(self, line):
        """
            Task: 7. Console 0.1
            Prints the string representation of an instance 
            based on the class name and id.
        """
        args = line.split()

        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.all_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        inst_id = args[1]

        instances_dict = storage.all()
        key = "{}.{}".format(class_name, inst_id)
        if key not in instances_dict:
            print("** no instance found **")
            return

        instance = instances_dict[key]
        print(instance)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
