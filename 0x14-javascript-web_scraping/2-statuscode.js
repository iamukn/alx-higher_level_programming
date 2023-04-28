#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, (err, response, body) => {
  if (response.statusCode) {
    console.log('code:', response.statusCode);
  }
  if (err) {
    console.log(err);
  }
});
