from os import getenv
import  models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class inheriting from BaseModel"""

    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade=['all', 'delete-orphan'],
                              backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """Returns the list of City instances associated to the current state
        """
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            all_cities = models.storage.all(City)
            return [city for city in all_cities.values() if city.state_id == self.id]
        return []
    
