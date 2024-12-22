import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    def do_greet(self, user):
        """greet the user"""
        if user:
            print(f'hi, {user}')
        else:
            print('hi')
    
    def do_EOF(self, line):
        return True
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()