#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    for (const m in movies) {
      const characters = movies[m].characters;
      for (const c in characters) {
        if (characters[c].includes('18')) {
          count++;
	}
      }
    }
    console.log(count);
  } else {
    console.log('Error: ' + response.statusCode);
  }
});
