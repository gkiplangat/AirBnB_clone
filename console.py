#!/usr/bin/env python3

"""
Command line interpreter for AirBnB
"""
import cmd
from models import storage


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
    
    def do_create(self, line):
        """
        Creates a new instance of BaseModel and saves it
        to a JSON file
        """
        if line:
            if line in self.__classes:
                new_object = self.__classes[line]()
                new_object.save()
                print(f"{new_object.id}")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(line):
        """
        Help message for the "create" command
        """
        print("Usage: create <class_name>")

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        arguments = line.split() if line else []
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arguments) != 2:
            print("** instance id missing **")
        else:
            objects_dict = storage.all()
            search_key = f'{arguments[0]}.{arguments[1]}'
            if search_key in objects_dict:
                print(objects_dict[search_key])
            else:
                print("** no instance found **")

    def help_show(line):
        """
        Prints the help message for the "show" command
        """
        print("Usage: show <class_name> <id> or <class>.show(<id>)")

    def do_destroy(self, line: str) -> None:
        """
        Deletes an instance based on the class name and id
        and saves changes to storage
        """
        arguments = line.split() if line else []
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arguments) != 2:
            print("** instance id missing **")
        else:
            objects_dict = storage.all()
            search_key = f"{arguments[0]}.{arguments[1]}"
            if search_key in objects_dict:
                del objects_dict[search_key]
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(line):
        """
        prints the help method for the "destroy" command
        """
        print("Usage: destroy <class_name> <id> or <class>.destroy(<id>)")
        print("Removes the specified class")

    def do_update(self, arg: str) -> None:
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = f"{arg_list[0]}.{arg_list[1]}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        setattr(objects[key], arg_list[2], arg_list[3])
        storage.save()

    def help_update(line):
        """
        prints help method for the update command
        """
        print(
            "Usage: update <class name> <id> <attribute name>"
            ' "<attribute value>"'
        )
        print(
            "Updates an instance of class_name and id by adding"
            " or updating attribute\n"
        )

    def do_all(self, line):
        arguments = line.split() if line else []
        objects_dict = storage.all()
        all = []
        if not arguments:
            for val in objects_dict.values():
                all.append(str(val))
            if len(all) >= 1:
                print(all)
        else:
            if arguments[0] not in self.__classes:
                print("** class doesn't exist **")
            for val in storage.all().values():
                if arguments[0] == val.to_dict()["__class__"]:
                    all.append(str(val))
            if len(all) >= 1:
                print(all)

    def help_all(line):
        """
        Prints the message for the "all" command
        """
        print("Usage: all or all <class> or <class>.all()")

    def default(self, line: str) -> None:
        """
        Method called when a command is not
        used as first argument
        """
        args = line.split(".") if line else []
        objects_dict = storage.all()
        try:
            cls = args[0]
            if len(args) > 1:
                comd = args[1]
            if not cls:
                print("** class name missing **")
            elif cls not in self.__classes:
                print("** class doesn't exist **")
            elif comd == "all()":
                self.do_all(cls)
            elif comd == "count()":
                count = 0
                for value in objects_dict.values():
                    val = value.to_dict()
                    if cls == val["__class__"]:
                        count += 1
                print(count)
            elif comd.startswith("show") or comd.startswith("destroy"):
                args = comd.split("(")
                comd = args[0]
                args = args[1].split(")")
                obj_id = args[0].strip('"').strip(")").strip('"')
                if comd == "show":
                    self.do_show(f"{cls} {obj_id}")
                elif comd == "destroy":
                    self.do_destroy(f"{cls} {obj_id}")

            elif comd.startswith("update"):
                args = comd.split("(")
                comd = args[0]
                curly_index = args[1].find("{")
                obj_id = args[1][:curly_index].strip(', ').strip('"')
                if not obj_id or args[1] == ")":  # or curly_index == -1:
                    print("** instance id missing **")
                elif not args[1].startswith('"') and '"' not in args[1]:
                    print("** no instance found **")
                else:
                    dict_args = args[1][curly_index:].split(")")
                    if dict_args[0].startswith('{') and dict_args[0].endswith("}"):
                        attr_dict = eval(dict_args[0])
                        for key, value in attr_dict.items():
                            self.do_update(f"{cls} {obj_id} {key} {value}")
                    else:
                        attr_name = dict_args[1].strip('"')
                        attr_value = dict_args[2].strip('"')
                        self.do_update(f"{cls} {obj_id} {attr_name} {attr_value}")
        except IndexError:
            print("Invalid!")

    def emptyline(self):
        """Handles empty lines"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
