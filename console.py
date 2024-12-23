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
        
        # Strips input of leading or trailing whitespaces
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

    def do_show(self, line):
        """Prints string format of an instance based on class name and id"""
        command_args = line.split()
        # Check if class name is provided
        if len(command_args) < 1:
            print('** class name missing **')
            return
        
        class_name = command_args[0]
        # Check if class exists
        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
        
        # Check if class id is provided
        if len(command_args) < 2:
            print('** instance id missing **')
            return
        
        class_id = command_args[1]
        key =f"{class_name}.{class_id}"

        # Check ifinstance exists
        all_objects = storage.all()

        if key not in all_objects:
            print('** instance id missing **')
            return
        
        # Print the instance
        print(all_objects[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        command_args = line.split()
        if len(command_args) < 1:
            print("** class name missing **")
            return
        
        class_name = command_args[0]
        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        
        if len(command_args) < 2:
            print('** instance id missing **')
            return
        
        class_id = command_args[1]
        key = f"{class_name}.{class_id}"

        # Check if instance exists
        all_objects = storage.all()
        if key not in all_objects:
            print('** no instance found **')
            return
        
        # Deletes the instance and save changes
        del all_objects[key]
        storage.save()

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