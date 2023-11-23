#!/usr/bin/python3
"""
Script to fetch and print City objects from the database hbtn_0e_14_usa,
displaying the city id, city name, and the corresponding state name.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))  # Connect to MySQL server
    Base.metadata.create_all(engine)  # Create tables based on defined models
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query and list all City objects with corresponding State names
    for instance in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])  # Print formatted results
