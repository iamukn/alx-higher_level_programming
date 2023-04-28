#!/usr/bin/node

const content = process.argv[2];

const fs = require('fs');

fs.readFile(content, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
}
);
