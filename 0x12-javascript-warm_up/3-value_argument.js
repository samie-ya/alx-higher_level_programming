#!/usr/bin/node

const av = process.argv.slice(1);
if (!(av[1])) {
  console.log('No argument');
} else {
  console.log(av[1]);
}
