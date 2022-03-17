#!/bin/bash
#This script that takes in a URL, request to that URL
curl -X POST 0.0.0.0:5000/catch_me -H "Content-Type: text/html" -d 'You got me!' | curl 0.0.0.0:5000/catch_me
