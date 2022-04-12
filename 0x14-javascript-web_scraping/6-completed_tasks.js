#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(1);

request(args[1], (error, response, body) => {
  let total = 0;
  if (error) {
    console.log(error);
  } else {
    const todo = JSON.parse(body);
    const list = [];
    for (const value of todo) {
      list.push(value.completed);
    }
    const listoflist = [];
    for (let i = 0; i < list.length; i += 20) {
      listoflist.push(list.slice(i, i + 20));
    }
    const result = [];
    for (const lists of listoflist) {
      for (const ls of lists) {
        if (ls === true) {
          total = total + 1;
        }
      }
      result.push(total);
      total = 0;
    }
    const number = [];
    for (let i = 1; i < 11; i++) {
      number.push(i);
    }
    const dict = {};
    number.forEach((k, i) => {
      dict[k] = result[i];
    });
    console.log(dict);
  }
});
