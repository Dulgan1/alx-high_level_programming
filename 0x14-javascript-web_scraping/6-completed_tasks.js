#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const taskD = {};
const list = [];
request(url, function (error, response, body) {
  if (error) {
    console.error('error: ' + error);
  }
  const todoList = JSON.parse(body);
  for (const i in todoList) {
    const task = todoList[i];
    if (task.completed === true) {
      list.push(task.userId);
    }
  }

  list.forEach((i) => { taskD[i] = (taskD[i] || 0) + 1; });
  console.log(taskD);
});
