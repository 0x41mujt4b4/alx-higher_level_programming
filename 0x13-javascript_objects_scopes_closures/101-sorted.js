#!/usr/bin/node
// function that returns the number of occurrences in a list
const { dict } = require('./101-data.js');

const newDict = {};
for (const key in dict) {
  const value = dict[key];
  if (newDict[value]) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}

console.log(newDict);
