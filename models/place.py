import models
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """Place class inheriting from BaseModel"""

    # Class attribtes
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # Reltionship for DBStorage
        reviews = relationship(
            'Review',
            cascade=['all', 'delete-orphan'],
            backref='place'
        )
    else:
        @property
        def reviews(self):
            """Returns the list of Reviews instances associated to current place"""
            all_reviews = models.storage.all(Review)
            return [
                review for review in all_reviews.values()
                if review.place_id == self.id
            ]
