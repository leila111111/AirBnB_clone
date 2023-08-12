#!/usr/bin/python3
""" Module containing console program """

import cmd
import re
import sys

# from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """creating class"""

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }
    prompt = "(hbnb) "
    # flag is used to track if the command line was successfully
    # handled by mo_cmdline method or not , 1 mean handled
    flag = 0

    def do_EOF(self, arg):
        """exit the program CTRL+d"""
        # print()
        return True

    def do_quit(self, arg):
        """exit the program with 'quit'"""
        return True

    def emptyline(self):
        """new empty line when pressing enter"""
        pass

    def do_create(self, arg):
        """creating new instance with 'create'"""

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if arg in HBNBCommand.classes:
                obj = HBNBCommand.classes[arg]()
                print(obj.id)
                obj.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instances"""

        if len(arg) == 0:
            print("** class name missing **")
        else:
            lists = arg.split(" ")
            if lists[0] in HBNBCommand.classes:
                if len(lists) > 1:
                    dicts = storage.all()
                    for key in dicts:
                        sp = key.split(".")
                        if sp[0] == lists[0] and sp[1] == lists[1]:
                            print(dicts[key])
                            return
                    print("** no instance found **")
                else:
                    print("** instance id missing **")

            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """destroy a given object based on class name and id"""

        if len(arg) == 0:
            print("** class name missing **")
        else:
            lists = arg.split(" ")
            if lists[0] in HBNBCommand.classes:
                if len(lists) > 1:
                    dicts = storage.all()
                    for key in dicts:
                        sp = key.split(".")
                        if sp[0] == lists[0] and sp[1] == lists[1]:
                            dicts.pop(key)
                            storage.save()
                            return
                    print("** no instance found **")
                else:
                    print("** instance id missing **")

            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""

        if len(arg) == 0:
            list_all = [str(val) for val in storage.all().values()]
            print(list_all)

        else:
            new_list = arg.split(" ")
            if new_list[0] in HBNBCommand.classes:
                list_sp_class = [
                    str(value)
                    for key, value in storage.all().items()
                    if type(value).__name__ == new_list[0]
                ]
                print(list_sp_class)

            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""

        if len(arg) == 0:
            print("** class name missing **")
        else:
            arg_sp = arg.split(" ")
            if arg_sp[0] in HBNBCommand.classes:
                if len(arg_sp) > 1:
                    n_key = str(arg_sp[0]) + "." + str(arg_sp[1])

                    if n_key in storage.all():
                        if len(arg_sp) > 2:
                            if len(arg_sp) > 3:
                                arg_sp_strip = arg_sp[3].strip("'").strip('"')
                                for key, obj in storage.all().items():
                                    if key == n_key:
                                        try:
                                            attr_val = float(arg_sp_strip)
                                        except ValueError:
                                            try:
                                                attr_val = int(arg_sp_strip)
                                            except ValueError:
                                                attr_val = arg_sp_strip

                                        setattr(obj, arg_sp[2], attr_val)
                                        obj.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")

                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def default(self, arg):
        """method is called when no valid command was found"""
        x = self.mo_cmdline(arg)
        if HBNBCommand.flag == 0:
            return cmd.Cmd.default(self, x)

    def mo_cmdline(self, arg):
        """method to modify the command line entred by the user"""

        # check if interactive or non interactive mode
        if not sys.stdin.isatty():
            print()

        # searching the content inside the parentheses
        match = re.search(r"\((.*?)\)", arg)
        point = "."

        # if the content is found it will return a match object
        if match and (point in arg):
            print("1")
            # assigning the content inside the parentheses
            # to a variable called  content
            content = match.group(1)
            if content == "":
                print("2")
                # match with User.all()
                match1 = re.match(r"(.*?)\.(.*?)\(\)", arg)
                if match1:
                    print("3")
                    cl1, cmd1 = match1.groups()
                    arg = f"{cmd1} {cl1}"
                    self.onecmd(arg)
                    HBNBCommand.flag = 1
                    return arg

            else:
                print("4")
                # match with User.destroy(id)
                match2 = re.match(r"(.*?)\.(.*?)\((.*?)\)", arg)
                if match2:
                    inputs = r"(.*?)\.(.*?)\((.*?), (.*?), (.*?)\)"
                    match3 = re.match(inputs, arg)
                    if match3:
                        print("7")
                        cl3, cmd3, i3, att_n, att_v = match3.groups()
                        i3 = i3.strip("'").strip('"')
                        att_n = att_n.strip("'").strip('"')
                        att_v = att_v.strip("'").strip('"')
                        arg = f"{cmd3} {cl3} {i3} {att_n} {att_v}"
                        self.onecmd(arg)
                        HBNBCommand.flag = 1
                        return arg
                    else:
                        cl, command, i = match2.groups()
                        i = i.strip("'").strip('"')
                        arg = f"{command} {cl} {i}"
                        self.onecmd(arg)
                        HBNBCommand.flag = 1
                        return arg
            return arg

    def do_count(self, arg):
        """method to count the number of instance of a class"""
        count = 0
        if len(arg) == 0:
            pass
        else:
            if arg in HBNBCommand.classes:
                for value in storage.all().values():
                    if type(value).__name__ == arg:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
