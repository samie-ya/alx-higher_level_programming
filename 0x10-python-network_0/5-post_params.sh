#!/bin/bash
# This script that sends a JSON POST request to a URL passed
curl -s -X POST -d "email: test@gmail.com" -d "subject: I will always be here for PLD" "$1"
