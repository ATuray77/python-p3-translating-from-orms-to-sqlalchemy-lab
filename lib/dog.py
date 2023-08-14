from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# engine = create_engine('sqlite:///:memory:')  # creates the engine that stores the data in the local directory;s db file
# Base.metadata.create_all(engine)  # Create all tables in the engine

# Session = sessionmaker(bind=engine)  # Creates the configured session class
# session = Session()   # creates the session object

def create_table(base, engine):
   base.metadata.create_all(engine)  # Create all tables in the engine

# Saves or adds the record to the session object
def save(session, dog):  
    session.add(dog)
    session.commit()    # Commits the record to the database

# Retrieving all the records from the Dog class
def get_all(session):  
    return session.query(Dog).all()

# Retrieving based on name
def find_by_name(session, name):  
    return session.query(Dog).filter(Dog.name == name).first()

    
# Retrieving data based on id
def find_by_id(session, id): 
    return session.query(Dog).filter(Dog.id == id).first()

# Retrieving data based on both name and breed
def find_by_name_and_breed(session, name, breed): 
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()







# from sqlalchemy import create_engine
# from models import Dog

# engine = create_engine('sqlite:///:memory:')

# def create_table(base):
#     sql = """
#         CREATE TABLE IF NOT EXISTS dogs (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             breed TEXT
#         );
#     """

#     return engine

# def save(session, dog):
#     session.add(dog)
#     session.commit()

#     return session

# def new_from_db(session, row):
#     return session.query(Dog).filter_by(id = row.id).first()

# def get_all(session):
#     return session.query(Dog)

# def find_by_name(session, name):
#     return session.query(Dog).filter_by(name = name).first()

# def find_by_id(session, id):
#     return session.query(Dog).filter_by(id = id).first()

# def find_by_name_and_breed(session, name, breed):
#     return session.query(Dog).filter_by(name = name, breed = breed).first()

# def update_breed(session, dog, breed):
#     dog.breed = breed
#     session.commit()
#     return session