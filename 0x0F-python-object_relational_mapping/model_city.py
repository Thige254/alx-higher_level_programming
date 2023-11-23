#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from model_state import Base  # Importing Base from model_state module
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)  # Unique, non-null, primary key column
    name = Column(String(128), nullable=False)  # String column with a maximum of 128 characters, non-null
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)  # Foreign key linking to states.id, non-null
