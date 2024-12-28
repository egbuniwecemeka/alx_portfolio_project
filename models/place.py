from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForiegnKey, Integer, Float

class Place(BaseModel, Base):
    """Place class inheriting from BaseModel"""

    # Class attribtes
    __tablename__ = 'places'
    city_id = Column(String(60),  ForiegnKey('cities.id'), nullable=False)
    user_id = Column(String(60),  ForiegnKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
