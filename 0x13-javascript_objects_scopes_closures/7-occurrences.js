#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let i in list) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return count;
}
