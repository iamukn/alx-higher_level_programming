#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const request = require('request');

request(url, (err, response, body) => {
  if (response) {
    const res = JSON.parse(body);
    console.log(res.title);
  }
  if (err) {
    console.log(err);
  }
});
