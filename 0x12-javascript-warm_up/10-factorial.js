#!/usr/bin/node
const arg = process.argv[2];
const x = +arg;
function factorial (a) {
  if (a === 0) return 1;
  return (a * factorial(a - 1));
}

if (!isNaN(x)) {
  console.log(factorial(x));
} else {
  console.log('1');
}
