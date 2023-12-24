#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Take MySQL username, password, and database name as command-line arguments
    username, password, database = sys.argv[1:]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select all states and order by states.id
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
