#!/usr/bin/python3
"""
Module that prints the first State object from database hbtn_0e_6_usa,
via SQLAlchemy.
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

    # Query the first State object by id
    first_state = session.query(State).order_by(State.id).first()

    # Check if states table is empty
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    # Close the session
    session.close()
