#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + movieID, (error, response, body) => {
  if (error) {
    return console.log('error: ' + error);
  }
  console.log(JSON.parse(body).title);
});
