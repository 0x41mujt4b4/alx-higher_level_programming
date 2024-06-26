#!/usr/bin/python3
"""model contain state table"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """state table class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
