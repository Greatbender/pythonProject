from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date, Boolean
from sqlalchemy.orm import relationship, backref

## A SQLalchemny engine that interacts with our db
engine = create_engine('sqlite:///movies_db', echo=False)
## SQLAlchemy ORM session bound to this engine
Session = sessionmaker(bind=engine)
session = Session()

## Base class for our classess definitions
Base = declarative_base()




class Days(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    day_number = Column(String)
    snowheight = Column(String)
    melting_hours = Column(String)

    def __init__(self, day_number, snowheight, melting_hours ):
        self.day_number = day_number
        self.snowheight = snowheight
        self.melting_hours = melting_hours



Base.metadata.create_all(engine)