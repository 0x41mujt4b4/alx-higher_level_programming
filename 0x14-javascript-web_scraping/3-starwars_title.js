#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});
