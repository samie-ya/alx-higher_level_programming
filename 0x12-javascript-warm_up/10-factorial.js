#!/usr/bin/node

function factorial (n) {
  if ((n === 0) || (n === 1) || isNaN(n) || n === undefined) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const av = process.argv.slice(1);
const num = parseInt(av[1]);
const fact = factorial(num);
console.log(fact);
