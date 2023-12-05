#!/bin/bash
# Bash script to send a JSON POST request to a URL with file contents
url=$1; file=$2; [ -z "$url" ] || [ -z "$file" ] && exit 1; curl -sX POST -H "Content-Type: application/json" -d "@$file" "$url"
