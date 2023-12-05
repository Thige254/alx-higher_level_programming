#!/bin/bash
# Bash script to display all HTTP methods accepted by server
url=$1; [ -z "$url" ] && exit 1; curl -sI -X OPTIONS "$url" | awk -F': ' '/Allow/ {print $2}'
