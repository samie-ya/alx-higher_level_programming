#!/bin/bash
#This script that takes in a URL, sends a POST request to the passed URL
curl -d 'POST params: \n\temail: test@gmail.com\n\tsubject: I will always be here for PLD' -H "Content-Type: application/json" -sX POST "$1"
