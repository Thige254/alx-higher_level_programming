#!/bin/bash
# Bash script that sends a request to a given URL n displays size of response body in bytes.

curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
