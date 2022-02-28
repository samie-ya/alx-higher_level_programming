#!/usr/bin/node

const av = process.argv.slice(1);
const word = 'C is fun';
if ((av.length === 1) || (isNaN(av[1]))) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < parseInt(av[1]); i++) {
  console.log(word);
}
