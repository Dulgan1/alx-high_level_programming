#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error)
  } else {
    let task = JSON.parse(body);
    let obj = {};
    for (let x in task) {
      if (task[x].completed) {
        if (obj[task[x].userID] === undefined) {
          obj[task[x].userID] = 1;
	} else {
          obj[task[x].userID]++;
	}
      }
    }
    console.log(obj);
  }
});
