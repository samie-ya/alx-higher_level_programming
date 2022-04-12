#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(1);
fs.readFile(args[1], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
