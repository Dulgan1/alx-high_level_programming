#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const x = +arg1;
const y = +arg2;

function add(a, b) {
  return  a + b;
}

if (!isNaN(x) && !isNaN(y)) {
  const sum = add(x, y);
  console.log(sum);
} else {
  console.log('NaN');
}
