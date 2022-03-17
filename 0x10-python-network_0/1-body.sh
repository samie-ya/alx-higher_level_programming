#!/bin/bash
#This cript request to a URL passed as an argument, displays only the status
if [ "$(curl -sI "$1" | head -n 1 | awk '{print $2}')" -eq "200" ]; then curl -s "$1"; fi
