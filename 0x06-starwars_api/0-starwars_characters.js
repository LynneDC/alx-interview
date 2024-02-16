#!/usr/bin/node

/**
 * Makes a series of requests to retrieve data from an array of URLs.
 * @param {string[]} arr - The array of URLs to request data from.
 * @param {number} i - The index of the current URL being requested.
 * @returns {void}
 */

const request = require('request');

const req = (arr, i) => {
  if (i === arr.length) return;
  request(arr[i], (err, response, body) => {
    if (err) {
      throw err;
    } else {
        console.log(JSON.parse(body).name);
        req(arr, i + 1);
    }
  });
};

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    } else {
      const chars = JSON.parse(body).characters;
      req(chars, 0);
    }
  }
);