#!/usr/bin/node
const numArray = process.argv.slice(2);

function secondBiggest (array) {
  if (array.length > 1) {
    array.sort(function (x, y) { return x - y; });
    return (array[array.length - 2]);
  } else {
    return (0);
  }
}

console.log(secondBiggest(numArray));
