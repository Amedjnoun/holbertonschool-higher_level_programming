#!/usr/bin/python3
"""
Module that contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """
    Class that represents a city in the cities table of hbtn_0e_14_usa database.

    Attributes:
        id (int): Unique id for the city, autogenerated
                and set as primary key, cannot be NULL
        name (str): name of the city, cannot be NULL
        state_id (int): Foreign key to states.id, cannot be NULL
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")
