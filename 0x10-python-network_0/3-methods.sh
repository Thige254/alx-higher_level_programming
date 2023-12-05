#!/bin/bash
# Bash script to display all HTTP methods accepted
url=$1; [ -z "$url" ] && exit 1; curl -sI -X OPTIONS "$url" | grep -i Allow | awk '{print $2}'
