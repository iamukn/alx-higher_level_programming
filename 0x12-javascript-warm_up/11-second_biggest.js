#!/usr/bin/node

const argc = process.argv.length;

const argv = process.argv.slice(2, argc);

const secondDigit = argv.sort((a, b) => a - b);

if (argc === 2) {
  console.log(0);
} else if (argc === 3) {
  console.log(0);
} else {
  console.log(secondDigit[argc - 4]);
}
