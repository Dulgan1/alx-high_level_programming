#!/usr/bin/node
const arg = process.argv[2];
const x = + arg;
if (!isNaN(x)) {
  console.log('My number: ' + x);
} else {
  console.log('Not a number');
}
