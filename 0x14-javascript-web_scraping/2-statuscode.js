#!/usr/bin/node
const request = require('request');
const urllink = process.argv[2];

request.get(urllink).on('response', (response) => {
  console.log('code: ' + response.statusCode);
});
