#!/usr/bin/python3
"""
Script to retrieve and display all State objects from the 'states' table in the database.
"""


import sys
# Importing the State class from the model_state module
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

    # Retrieve all State objects from the 'states' table, ordered by State.id
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
