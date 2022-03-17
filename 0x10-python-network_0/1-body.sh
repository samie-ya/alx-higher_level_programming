#!/bin/bash
#This script that takes in a URL, GET request to that URL, and displays
STATUS=$(curl -s -o /dev/null -w '%{http_code}' "$1")
if [ $STATUS -eq 200 ]
then
    curl -s "$1"
fi
