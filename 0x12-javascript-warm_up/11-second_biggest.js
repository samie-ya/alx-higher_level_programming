#!/usr/bin/node

const av = process.argv.slice(1);

function list () {
  if (av.length === 1 || av.length === 2) {
    return (0);
  }
  const newList = [];
  for (let i = 1; i < av.length; i++) {
    newList.push(parseInt(av[i]));
  }
  newList.sort(function (a, b) {
    return a - b;
  });
  const len = newList.length;
  return (newList[len - 2]);
}
const lt = list();
console.log(lt);
