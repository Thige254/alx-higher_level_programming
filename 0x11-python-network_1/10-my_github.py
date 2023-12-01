#!/usr/bin/python3
"""
Uses GitHub API to display user id using Basic Authentication
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    auth = (username, token)

    response = requests.get(url, auth=auth)

    try:
        user_info = response.json()
        user_id = user_info.get('id')
        if user_id is not None:
            print(user_id)
        else:
            print("Authentication failed.Try Again")
    except ValueError:
        print("Not a valid JSON")

