#!/bin/bash
# Bash script to send a POST request with variables to a URL and display the body of the response
url=$1; [ -z "$url" ] && exit 1; curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$url"
