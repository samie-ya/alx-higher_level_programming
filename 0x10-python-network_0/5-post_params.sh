#!/bin/bash
# This script that sends a JSON POST request to a URL passed
curl -d "@$1" -H "Content-Type: application/json" -sX POST "$1"
