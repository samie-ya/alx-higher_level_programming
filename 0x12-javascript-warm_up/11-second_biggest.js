#!/usr/bin/node

const av = process.argv.slice(1);

if (!(av[1]) || av.length === 2) {
  console.log(0);
}
function list () {
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
