#!/bin/bash
#This cript request to a URL passed as an argument, displays only the status
if [ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ]; then curl -s "$1"; fi;
