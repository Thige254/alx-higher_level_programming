#!/usr/bin/python3
""" Start link class to table in the database.
This script defines the State class and creates the corresponding table
in the MySQL database using SQLAlchemy.
"""

import sys
# Importing the State class from the model_state module
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./script_name.py <username> <password> <database_name>")
        sys.exit(1)

    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the table in the database based on the defined State class
    Base.metadata.create_all(engine)

    # Just for me...: Provide a success message
    print("Table 'states' created successfully.")
