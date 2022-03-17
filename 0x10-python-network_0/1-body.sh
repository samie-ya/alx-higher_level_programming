#!/bin/bash
#This cript request to a URL passed as an argument, displays only the status
curl -sLX GET "$1"
