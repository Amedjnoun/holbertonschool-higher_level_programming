#!/usr/bin/python3
"""
Module that adds the State object "Louisiana"
to database hbtn_0e_6_usa, via SQLAlchemy.
"""
import sys
from model_state import Base, State
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

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new State to the session and commit
    session.add(new_state)
    session.commit()

    # Print the new state id
    print(new_state.id)

    # Close the session
    session.close()
