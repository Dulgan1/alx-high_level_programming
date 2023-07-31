#!/usr/bin/node

const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(file, body, 'utf8', (error) => {
      console.log(error);
    });
  } else {
    console.log('Error: ' + response.statusCode);
  }
});
