#!/usr/bin/python3
"""Module that contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """Class definition of a City

    Attributes:
        __tablename__ (str): The name of the MySQL table
        id (int): The city's id (primary key)
        name (str): The city's name
        state_id (int): Foreign key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
