#!/usr/bin/node

const x = process.argv[2];
const parse = parseInt(x, 10);
if (parse) {
  const count = parse;
  let i;
  for (i = 0; i < count; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
