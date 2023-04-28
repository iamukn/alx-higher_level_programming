#!/usr/bin/node

const url = process.argv[2];

const id = 'https://swapi-api.alx-tools.com/api/people/18/';

const request = require('request');

request(url, (err, res, body) => {
  if (res) {
    const js = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < js.results.length; i++) {
      for (let j = 0; j < js.results[i].characters.length; j++) {
        if (js.results[i].characters[j] === id) {
          count++;
        }
      }
    }

    console.log(count);
  }
  if (err) {
    console.log(err);
  }
});
