#!/usr/bin/node

const args = process.argv.slice(1);
const request = require('request');
const fs = require('fs');
request(args[1]).pipe(fs.createWriteStream(args[2]));
