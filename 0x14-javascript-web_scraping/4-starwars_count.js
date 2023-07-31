#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (reponse.statusCode === 200) {
    let movies = JSON.parse(body).results;
    for (let m in movies) {
      let characters = movies.m.characters;
      for (let c in characters) {
        if (characters.c.includes('18')) {
          count++;
	}
      }
    }
    console.log(count);
  } else {
    console.log('Error: ' + response.statusCode);
  }
});
