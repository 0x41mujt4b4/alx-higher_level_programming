#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request(character, (err, res, body) => {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
