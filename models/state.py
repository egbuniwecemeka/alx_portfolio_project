from os import getenv
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class inheriting from BaseModel"""
    # Public class attribute
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state',
                              cascade='all delete-orphan')
    else:
        name = ""   
    
    @property
    def cities(self):
        """Returns the list of City instances
            where state_id equals current id
        """
        cities = list()
        for _id, city in models.storage.all(City).items():
            if city.state_id == self.id:
                cities.append(city)
        return cities
