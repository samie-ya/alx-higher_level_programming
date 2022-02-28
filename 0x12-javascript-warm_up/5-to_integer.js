#!/usr/bin/node

const av = process.argv.slice(1);
const num = parseInt(av[1]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ', num);
}
