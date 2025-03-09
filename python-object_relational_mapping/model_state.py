#!/usr/bin/python3
"""Module that contains the class definition of a State"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class definition of a State

    Attributes:
        __tablename__ (str): The name of the MySQL table
        id (int): The state's id
        name (str): The state's name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
