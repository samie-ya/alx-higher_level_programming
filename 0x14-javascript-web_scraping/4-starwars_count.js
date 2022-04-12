#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(1);
request(args[1], (error, response, body) => {
  let total = 0;
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).results;
    for (const res of result) {
      const character = res.characters;
      for (const chara of character) {
        const actor = 'https://swapi-api.hbtn.io/api/people/18/';
        if (chara === actor) {
          total = total + 1;
        }
      }
    }
  }
  console.log(total);
});
