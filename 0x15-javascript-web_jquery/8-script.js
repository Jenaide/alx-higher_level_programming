#!/usr/bin/node
const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json'

$.getJSON(url, function (data) {
  let titles = data.titles;
  $('UL#list_movies').text(data);
});
