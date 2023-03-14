#!/usr/bin/node
const argvv = process.argv.length;
if ((argvv <= 2)) {
  console.log('No argument');
} else if ((argvv === 3)) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
