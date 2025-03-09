#!/usr/bin/python3
#!/usr/bin/python3
"""Script that changes the name of a State object"""
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

    # Query state with id=2
    state = session.query(State).filter_by(id=2).first()

    # Update state name if found
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
