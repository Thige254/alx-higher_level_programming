#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa."""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Use a single execute() to perform the JOIN and retrieve data
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               INNER JOIN states ON states.id = cities.state_id"""
    cur.execute(query)

    # Fetch all the rows
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
