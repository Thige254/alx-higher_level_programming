#!/bin/bash
# Bash script to make a request to 0.0.0.0:5000/catch_me and cause the server to respond with "You got me!"
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me --header "Host: 0.0.0.0:5000"
