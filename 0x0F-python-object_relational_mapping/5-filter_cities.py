#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa."""


import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Get the state name from command-line argument
    state_name = sys.argv[4]

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
