#!/bin/bash
# Bash script to send a GET request to a URL and display the body of the response
url=$1; [ -z "$url" ] && exit 1; response=$(curl -sI "$url"); status_code=$(echo "$response" | grep -iE "^HTTP/[0-9.]+ ([0-9]+)" | awk '{print $2}'); [ "$status_code" = "200" ] && curl -s "$url" || echo "Request failed with status code: $status_code"
