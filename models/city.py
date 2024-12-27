from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """City class inheriting from BaseModel"""
    state_id = ""
    name = ""
