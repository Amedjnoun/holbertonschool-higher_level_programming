#!/usr/bin/python3
"""
Module that prints all the cities from database hbtn_0e_14_usa,
via SQLAlchemy.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                          .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                          pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all City objects with their State
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Print cities with their state
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
