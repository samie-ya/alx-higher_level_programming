#!/bin/bash
#This script  takes in a URL, displays all HTTP methods the server will accept
curl -sX "OPTIONS" "$1" -I | awk '/Allow/ {print $2}'
