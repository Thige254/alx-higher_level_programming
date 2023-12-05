#!/bin/bash
# Bash script to send a GET request with a custom header to a URL
url=$1; [ -z "$url" ] && exit 1; curl -sH "X-School-User-Id: 98" "$url"
