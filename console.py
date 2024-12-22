import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb)'

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """Exits the interpreter on EOF"""
        print()
        return True

    def emptyline(self):
        """Does nothing on empty input"""
        pass

    def help_quit(self):
        """Help information for quit"""
        print('Exits the program. Usage: quit')
    
    def help_EOF(self):
        """Help information for EOF"""
        print('Exits interpreter using EOF (Ctrl+D). Usage: EOF')
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()