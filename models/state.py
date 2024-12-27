from os import getenv
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """State class inheriting from BaseModel"""
    name = ""
