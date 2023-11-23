#!/usr/bin/python3
""" Script to link the State class to the 'states' table in the MySQL database."""

import sys
from model_state import Base, State  # Importing the State class from the model_state module
from sqlalchemy import create_engine


if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the 'states' table in the database based on the State class
    Base.metadata.create_all(engine)
