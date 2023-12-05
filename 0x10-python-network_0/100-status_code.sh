#!/bin/bash
# Bash script to send a request to a URL and display only the status code of the response
url=$1; [ -z "$url" ] && exit 1; response=$(curl -s -o /dev/null -w "%{http_code}" "$url"); echo "$response"
