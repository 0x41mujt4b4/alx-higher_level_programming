#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const todos = JSON.parse(body);
  const results = {};
  for (const todo of todos) {
    if (todo.completed) {
      if (results[todo.userId]) {
        results[todo.userId]++;
      } else {
        results[todo.userId] = 1;
      }
    }
  }
  console.log(results);
});
