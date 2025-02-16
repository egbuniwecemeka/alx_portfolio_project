from json import dump, load
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.cart import Cart

classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Place": Place, "Amenity": Amenity, "Review": Review, "Cart": Cart}


class FileStorage:
    """serializes instances to JSON and deserialize JSON to instances"""

    # Private class attributes
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """returns __objects dictionary"""
        if cls is None:
            return self.__objects
        
        if isinstance(cls, str):
            try:
                # Dynnmaically import class
                cls = eval(cls)
            except NameError:
                return {}
        
        if cls:
            filtered_objects = {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
            return filtered_objects
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
    
    def delete(self, obj=None):
        """Deletes an object from _objects instances"""
        if obj is None:
            return
        
       # Build the key to check for the object in _objects
        key = f"{obj.__class__.__name__}.{obj.id}"

        # Deletes the object if key found in _objects
        if key in self.__objects:
            del self.__objects[key]
    
    def close(self):
        """Reloads objects from the JSON file"""
        self.reload()

    def get(self, cls, id):
        """Retrieves an object based on its class and ID"""
        if cls is None or id is None:
            return None
        
        # Construct key to query object in __objects
        key = f'{cls.__name__}.{id}'

        # Return the object if it exists in __objects, otherwise return None
        return self.__objects.get(key, None)
    
    def count(self, cls=None):
        """Returns number of objects for a given class, otherwise it returns all objects"""
        if cls is None:
            return len(self.__objects)
        
        # Counts objects of the specified class
        return len(self.all(cls))
    
    def get_user_by_username(self, username):
        """ Retrieves the object when username matches """
        for obj in self.all('User').values():
            if obj.username == username:
                return obj
        
        return None
