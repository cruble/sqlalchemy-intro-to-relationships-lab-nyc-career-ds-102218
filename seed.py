from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below

tom = Actor(name = "Tom Hanks")
gwyn = Actor(name = "Gwyneth Paltrow")
dustin = Actor(name = "Dustin Hoffman")

tom.roles = [Role(character='Forrest Gump'), Role(character='Jim Lovell'), Role(character = "Woody"), Role(character = "Robert Langdon")]
gwyn.roles = [Role(character = 'Pepper Potts'), Role(character = "Margot Tenenbaum")]
dustin.roles = [Role(character = "Ratso"), Role(character = "Tootsie")]

session.add_all([tom, gwyn, dustin])
session.commit() 

# Base.metadata.tables will get you the columns

