from os import getenv
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.base_model import Base


class DBStorage:
    """DBStorage class"""

    # Private attributes
    __engine = None
    __session = None

    def __init__(self):
        """Creates the SQLAlchemy engine linked to MySQL database"""
        # Environment variables
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        db = getenv('HBNB_MYSQL_DB')

        # Creates the engine with specified connection parameters
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}:3306/{db}',
            pool_pre_ping=True)

        # Drop all tables if in test environment
        if getenv('HBNB_ENV') == 'test':
            return self.drop_all_tables()

    def drop_all_tables(self):
        """Drop all tables in the database"""
        inspector = inspect(self.__engine)
        for table_name in inspector.get_table_names():
            self.__engine.execute(f'DROP TABLE IF EXISTS {table_name}')
    
    def all(self, cls=None):
        """Query the current database session (self.__session) and return all objects
           depending on the class name (cls). If its None return all objects
           from all classes
        """
        objects = {}
        if cls is None:
            # Query all objects from all classes
            for class_obj in Base.__subclasses__():   # Get all subclasses of Base
                 for obj in self.__session.query(class_obj).all():
                     objects[f"{class_obj.__name__}.{obj.id}"] = obj
        else:
            # Query all objects of the specified class
            objs = self.__session.query(cls).all()
            for obj in objs:
                objects[f"{cls.__name__}.{obj.id}"] = obj
        
        return objects
    
    def new(self, obj):
        """Adds the object to the current database session (self.__session)"""
        if obj is not None:
            self.__session.add(obj)
        
    def save(self):
        """Commit all changes of the current database session (self.session)"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Deletes obj from the current sesssion if its not empty"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and sets up the current session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        """Closes the current session"""
        self.__session.remove()