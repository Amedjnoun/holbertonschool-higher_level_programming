#!/usr/bin/python3
"""Script that adds the State object "Louisiana" to the database"""
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

    # Create new State
    new_state = State(name="Louisiana")

    # Add to session and commit
    session.add(new_state)
    session.commit()

    # Print new state ID
    print(new_state.id)

    # Close session
    session.close()
