import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb)'

    def do_create(self, line):
        """Creates an instance of BaseModel and saves it"""
        if not line.strip():
            print('** class name missing **')
            return
        
        # Split input into class name and parameters
        args = line.split()
        class_name = args[0]

        try:
            # Dynamically retrieve class name
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        
        # create an instance of the class
        new_model = cls()

        for param in args[1:]:
            if "=" in param:
                key, value = param.split("=", 1)

                # Handles value types
                if value.startswith('"') and value.endswith('"'):   # String
                    value = value[1:-1].replace("\\\"", '\"').replace("_", " ")
                elif "." in value:  # Float
                    try:
                        value = float(value)
                    except ValueError:
                        continue
                else:   # Integer
                    try:
                        value = int(value)
                    except ValueError:
                        continue

                # Set the new attribtes on the instance
                setattr(new_model, key, value)

        # Saves instance to storage
        new_model.save()
        # Print unique id of instance
        print(new_model.id)

    def do_show(self, line):
        """Prints string format of an instance based on class name and id"""
        if not line.strip():
            print("** class name missing **")
            return
        
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
        if not line.strip():
            print("** class name missing **")
            return
        
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

    def do_all(self, line):
        """Prints string representation of all instances"""
        all_objects = storage.all()
        # if no class name, print all instances
        if not line.strip():
            print([str(obj) for obj in all_objects.values()])
            return
        
        # Validate the class name
        class_name = line.strip()
        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        
        # Filters instances by class and print
        result = [str(obj) for obj in all_objects.values()
            if isinstance(obj, cls)]
        print(result)

    def do_update(self, line):
        """Updates an instance based on class name and id"""
        command_args = line.split()

        # check for empty input devoid of whitespaces
        if not line.strip():
            print('** class name missing **')
            return
        
        # check for class name
        if len(command_args) < 1:
            print('** class name missing **')
            return
        
        # Validate class name
        class_name = command_args[0]
        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        
        # Check for instance id
        if len(command_args) < 2:
            print('** instance id missing **')
            return
        
        class_id = command_args[1]
        key = f"{class_name}.{class_id}"
        all_objects = storage.all()

        # Check if instance exists
        if key not in all_objects:
            print('** instance id missing **')
            return
        
        # Check for attribute name
        if len(command_args) < 3:
            print('** attribute name missing **')
            return
        
        attribute_name = command_args[2]

        # Check for attribute value
        if len(command_args) < 4:
            print('** value missing **')
            return
        
        attribute_value = command_args[3].strip('"')

        # Prevent updating restricted attributes
        if attribute_name in {"id", "created_at", "updated_at"}:
            return
        
        # Pair attribute value to correct type
        instance = all_objects[key]
        if attribute_name in instance.__class__.__dict__:
            attribute_type = type(getattr(instance.__class__, attribute_name))
            try:
                attribute_value = attribute_type(attribute_value)
            except NameError:
                print(f"Invalid vale type for {attribute_name}")
                return
        
        # Update the instance and save
        setattr(instance, attribute_name, attribute_value)
        instance.save()
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

    def help_destroy(self):
        """Help information for destroy command"""
        print('Usage: destroy <className> <classID>')

    def help_all(self):
        """Help information from all command"""
        print('Usage: all <className> || all')

    def help_update(self):
        """Help information for update command"""
        print('Usage: update <class name> <id> <attribute name>\
              "<attribute value>"')

    def help_quit(self):
        """Help information for quit"""
        print('Exits the program. Usage: quit')
    
    def help_EOF(self):
        """Help information for EOF"""
        print('Exits interpreter using EOF (Ctrl+D). Usage: EOF')
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()
