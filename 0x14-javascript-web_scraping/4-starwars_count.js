#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    return console.log('error: ' + error);
  }

  const r = JSON.parse(body).results;
  for (const x in r) {
    const characterS = r[x].characters;
    for (const i in characterS) {
      if (characterS[i].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
