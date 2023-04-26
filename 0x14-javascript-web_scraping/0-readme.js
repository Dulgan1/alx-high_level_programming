#!/usr/bin/node
const fs = require('fs');

let file = process.argv[2];

fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
