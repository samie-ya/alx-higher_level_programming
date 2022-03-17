#!/bin/bash
#This script that takes in a URL, request to that URL, and displays body size
curl -I "$1" | grep Accept-Ranges: bytes | curl -s "$1"
