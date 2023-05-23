#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const Url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request.get(Url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log('Request failed with status code: ', response.statusCode);
  } else {
    const movie = JSON.parse(body);
    console.log('Title: ', movie.title);
  }
});
