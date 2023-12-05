#!/bin/bash
# This Bash script sends a GET request to a given URL and displays the body of the response for a 200 status code.

curl -sLw "\n%{http_code}" "$1" | grep -w "200" | cut -d$'\n' -f1
