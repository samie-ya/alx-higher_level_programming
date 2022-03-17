#!/bin/bash
# This script that takes in a URL, request to that URL, using X-School-User-Id
curl -s -H "X-School-User-Id: 98" "$1"
