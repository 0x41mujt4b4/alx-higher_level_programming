from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column("name", string(128), nullable=False)
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
