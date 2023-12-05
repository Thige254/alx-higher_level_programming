#!/bin/bash
# Bash script to display all HTTP methods accepted by a server
url=$1
[ -z "$url" ] && exit 1
curl -sI --request-target "*" "$url" | grep -i Allow | cut -d' ' -f2-
