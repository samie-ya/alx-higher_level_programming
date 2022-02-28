#!/usr/bin/node

const av = process.argv.slice(1);
const word = 'X';
if ((av.length === 1) || (isNaN(av[1]))) {
  console.log('Missing size');
}
for (let i = 0; i < parseInt(av[1]); i++) {
  for (let j = 0; j < parseInt(av[1]); j++) {
    process.stdout.write(word);
  }
  process.stdout.write('\n');
}
