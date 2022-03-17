#!/bin/bash
#This cript request to a URL passed as an argument, displays only the status
curl -s -o /dev/null -w "%{http_code}\n" "$1"
