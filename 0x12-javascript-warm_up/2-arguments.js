#!/usr/bin/node
const arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else if (process.argv[3] !== undefined) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
