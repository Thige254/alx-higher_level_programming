#!/bin/bash
# Bash script to send a DELETE request to a URL
url=$1; [ -z "$url" ] && exit 1; curl -sX DELETE "$url"
