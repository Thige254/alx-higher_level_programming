#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

def get_cities_by_state(username, password, database, state_name):
    """
    Retrieve and print the names of cities in the specified state.

    Parameters:
    - username: MySQL username
    - password: MySQL password
    - database: Database name
    - state_name: Name of the state to search for

    Returns:
    None
    """
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = """SELECT cities.name
               FROM cities
               INNER JOIN states ON states.id = cities.state_id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""

    # Execute the query with the state name as a parameter
    cur.execute(query, (state_name,))

    # Fetch all the rows
    rows = cur.fetchall()

    # Display the results
    if rows:
        # Join city names with commas for better presentation
        city_names = ", ".join(row[0] for row in rows)
        print(city_names)
    else:
        print("(no matching cities)")

    # Close the cursor and database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    # Ensure correct number of command-line arguments
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Get command-line arguments
    username, password, database, state_name = sys.argv[1:5]

    # Call the function to get cities by state
    get_cities_by_state(username, password, database, state_name)
