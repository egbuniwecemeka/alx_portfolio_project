#!/usr/bin/python3
"""Foundational class serving as a blueprint for other classes"""

# Imports
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, String

class BaseModel:
    """BaseModel(Parent) class that defines attribute/methods for other classes"""

    # Class Attributes (SQLAlchemy Columns)
    # id - unique identifier for each instance
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    # created_at - timestamp for recording instance creation
    created_at = Column(DateTime, default=(datetime.utcnow()), nullable=False)
    # updated_at - timestamp for recording instance update(s)
    updated_at = Column(DateTime, default=(datetime.utcnow()), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes a new base model based on arguments passed
        
           Args:
                args - not used
                kwargs - arguments for BaseModel constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                # Convert string timstamp format to datetime objects
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                # Ignores __class__ key if present & sets instance attribute
                if key != '__class__':
                    setattr(self, key, value)

                # Handle missing attributes
                if "id" not in kwargs:
                    self.id = str(uuid4())
                if "created_at" not in kwargs:
                    self.created_at = datetime.now()
                if "updated_at" not in kwargs:
                    self.updated_at = datetime.now()
        # If kwarg is empty
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of class name/attributes"""
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"
    
    def save(self):
        """Updates current datetime of update_at attribute"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """returns a dictionary containing key/value of __dict__ instance"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({self.__class__: self.__class__.__name__})
        dictionary['created_at'] = datetime.isoformat()
        dictionary['updated_at'] = datetime.isoformat()

        return dictionary
