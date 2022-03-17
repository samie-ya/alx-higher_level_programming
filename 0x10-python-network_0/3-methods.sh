#!/bin/bash
#This script  takes in a URL, displays all HTTP methods the server will accept
curl -sX OPTIONS "$1" -I | grep Allow | cut -d ' ' -f 2 
