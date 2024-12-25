from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel
        It represents a user with email, password, first_name and last_name
    """
    # Public attribute
    email = ""
    password = ""
    first_name = ""
    last_name = ""