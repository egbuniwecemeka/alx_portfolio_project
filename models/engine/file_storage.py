from json import dump, load
from os.path import exists
from models.base_model import BaseModel
from models.user import User

classes = {"BaseModel": BaseModel, "User": User}


class FileStorage:
    """serializes instances to JSON and sederialize JSON to instances"""

    # Private class attributes
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns __objects dictionary"""
        return self.__objects
    
    def new(self, obj):
        """sets in _objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as file:
            # Convert each object in __objects to a dictionary
            dump({k: v.to_dict() for k, v in self.__objects.items()}, file)
    
    def reload(self):
        """Deserializes the JSON file to __objects"""
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = load(file)
                for key, value in data.items():
                    class_name = value.get('__class__')
                    if class_name in classes:
                        self.__objects[key] = classes[class_name](**value)
