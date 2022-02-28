#!/usr/bin/node

function add (a, b) {
  return (parseInt(a) + parseInt(b));
}

const av = process.argv.slice(1);
const total = add(av[1], av[2]);
console.log(total);
