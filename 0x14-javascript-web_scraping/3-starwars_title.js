#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(1);
const urlpath = 'https://swapi-api.hbtn.io/api/films/' + args[1];

request(urlpath, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
