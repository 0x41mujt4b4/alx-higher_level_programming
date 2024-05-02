#!/usr/bin/python3
"""model contain state table"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """state table class"""
    __tablename__ = 'states'
    id = Column("id", Integer(11), primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name