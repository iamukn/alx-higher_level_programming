#!/usr/bin/node

const filename = process.argv[3];
const url = process.argv[2];

const fs = require('fs');
const request = require('request');

request(url, (err, res, body) => {
  fs.writeFile(filename, body, 'UTF-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
  if (err) {
    console.log(err);
  }
});
