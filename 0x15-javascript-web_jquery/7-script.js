#!/usr/bin/node
const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.getJSON(url, function (data) {
  let name = data.name;
  $('DIV#character').text(name);
});
