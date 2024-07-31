#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const movies = JSON.parse(body).results;
  console.log(movies.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0));
});
