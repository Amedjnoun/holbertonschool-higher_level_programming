#!/usr/bin/python3
"""Script that prints all City objects from the database"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query cities and join with states
    results = session.query(State, City).join(
        City, State.id == City.state_id).order_by(City.id).all()

    # Display results
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
