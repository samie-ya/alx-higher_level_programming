#!/bin/bash
#This script that takes in a URL, sends a POST request to the passed URL
curl -sX POST -H "Content-Type: text/html" -d '{"email": test@gmail.com, "subject": I will always be here for PLD}' "$!"
