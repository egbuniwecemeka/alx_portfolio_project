from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


if getenv('HBNB_TYPE_STORAGE') == 'db':
    # Create a unique instance of DBStorage
    storage = DBStorage()
    # Call reload method on DBStorage instance
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
