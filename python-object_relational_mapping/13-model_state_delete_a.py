#!/usr/bin/python3
"""Script that deletes State objects with a name containing letter a"""
import sys
from model_state import Base, State
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

    # Query states containing letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state
    for state in states:
        session.delete(state)

    # Commit changes
    session.commit()

    # Close session
    session.close()
