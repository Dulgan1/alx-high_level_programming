#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const num = process.argv[2];
const dict = {};

request(url + num, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const charLst = JSON.parse(body).characters;
  for (const i in charLst) {
    request(charLst[i], (error, response, body) => {
      if (error) {
        console.error('error:', error);
      }
      dict[i] = JSON.parse(body).name;
      const len1 = Object.keys(dict).length;
      if (charLst.length === len1) {
        for (const k in dict) {
          console.log(dict[k]);
        }
      }
    });
  }
});
