#!/usr/bin/node

const args = process.argv.slice(1);
const request = require('request');
request
  .get(args[1])
  .on('response', (response) => {
    console.log('code:', response.statusCode);
  });
