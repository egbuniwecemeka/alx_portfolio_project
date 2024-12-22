import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    def do_greet(self, line):
        print('Hello')
    
    def do_EOF(self, line):
        return True
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()