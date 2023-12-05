#!/usr/bin/python3
"""
Script to list all State objects containing the letter 'a' from the 'states' table
in the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create the 'states' table in the database based on the State class
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and list all State objects containing the letter 'a'
    for state in session.query(State).filter(State.name.like('%a%')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
