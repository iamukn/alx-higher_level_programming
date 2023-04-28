#!/usr/bin/node

const doc = process.argv[2];
const content = process.argv[3];

const fs = require('fs');

fs.writeFile(doc, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
