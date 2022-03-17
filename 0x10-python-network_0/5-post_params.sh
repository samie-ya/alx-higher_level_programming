#!/bin/bash
#This script that takes in a URL, sends a POST request to the passed URL
curl -sX POST "$1" -H "Content-Type: application/json" -d '{"email": test@gmail.com, "subject": I will always be here for PLD}'
