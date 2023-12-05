#!/bin/bash
# Bash script to send a request to a URL and display the size of the response body
curl -sI "$1" | grep -iE "^Content-Length:" | awk '{print $2}' | tr -d '\r\n'
