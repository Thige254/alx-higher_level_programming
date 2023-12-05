#!/usr/bin/python3
"""
Sends POST request to a URL with an email as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(f"Your email is: {email}")
    print(response.text)
