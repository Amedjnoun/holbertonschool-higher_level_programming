#!/usr/bin/python3
"""
Module that print State object with the name passed as argument
from database hbtn_0e_6_usa, via SQLAlchemy.
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

    # Query the State object with the specified name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print state id if found, otherwise print "Not found"
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

    # Close the session
    session.close()
