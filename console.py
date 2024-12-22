import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb)'

    def do_create(self, line):
        """Creates an instance of BaseModel and saves it"""
        if not line.strip():
            print('** class name missing **')
            return
        
        class_name = line.strip()
        try:
            # Dynamically retrieve class name
            cls = eval(class_name)
            # create an instance of the class
            new_model = cls()
            # Saves instance to storage
            new_model.save()
            # Print unique id of instance
            print(new_model.id)
        except NameError:
            print("** class doesn't exist **")

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

    def help_create(self):
        """Help information for create command"""
        print('Usage: create <className>')

    def help_quit(self):
        """Help information for quit"""
        print('Exits the program. Usage: quit')
    
    def help_EOF(self):
        """Help information for EOF"""
        print('Exits interpreter using EOF (Ctrl+D). Usage: EOF')
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()