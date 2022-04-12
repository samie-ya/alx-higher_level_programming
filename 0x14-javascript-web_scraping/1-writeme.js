#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(1);
fs.writeFile(args[1], args[2], 'utf-8', err => {
  if (err) {
    console.error(err);
  }
});
