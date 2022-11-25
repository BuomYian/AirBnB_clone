#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "


    def do_EOF(self, line):
        """end of file: exit the program"""
        return True

    def do_all(self, className):
        """Print string of an instance based on class name"""
        pass

    def do_create(self, className):
        """Creates a new instance of BaseModel"""
        pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        pass

    def do_quit(self, line):
        """Exit the program"""
        exit()

    def do_show(self, className):
        """Print string representation of an instance"""
        pass

    def do_update(self, classname):
        """Updates an instance based on the class name"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
