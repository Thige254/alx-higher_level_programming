#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Get the state name from command-line argument
    match = sys.argv[4]

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name LIKE %(match)s"
    cur.execute(query, {'match': match})

    # Fetch all the rows
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
