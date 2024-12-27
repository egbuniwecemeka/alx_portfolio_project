from os import getenv
from models import storage
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class inheriting from BaseModel"""

    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all delete-orphan',
                              backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """Returns the list of City instances
            where state_id euals to the current State.id
        """
        all_cities = storage.all(City)
        return [city for city in all_cities.values() if city.state_id == self.id]
