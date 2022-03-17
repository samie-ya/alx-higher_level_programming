#!/bin/bash
#This script that takes in a URL, request to that URL
curl -sX PUT 0.0.0.0:5000/catch_me -H "Content-Type: text/html" -d 'You got me!'
