#!/usr/bin/node

const av = process.argv.slice(1);

if (av.length === 1) {
  console.log('No argument');
} else if (av.length === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
