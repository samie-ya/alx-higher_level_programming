#!/usr/bin/node

const av = process.argv.slice(1);
if (isNaN(parseInt(av[1]))) {
  console.log('Not a number');
} else {
  console.log('My number: ', parseInt(av[1]));
}
