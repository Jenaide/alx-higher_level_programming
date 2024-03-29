#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log('Request failed with status code: ', response.statusCode);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) {
    } else {
      console.log('Successfully saved the webpage contents to ', filePath);
    }
  });
}
});
