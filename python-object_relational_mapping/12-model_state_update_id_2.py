#!/usr/bin/python3
"""
Module that changes the name of a State object
from the database hbtn_0e_6_usa, via SQLAlchemy.
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

    # Query the State object with id=2
    state = session.query(State).filter_by(id=2).first()

    # Update the state name and commit
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
