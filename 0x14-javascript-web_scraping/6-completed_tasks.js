#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log('Request failed with status code: ', response.statusCode);
  } else {
    const toDo = JSON.parse(body);
    const completedTasksByUser = {};

    toDo.forEach((toDo) => {
      if (toDo.completed) {
        if (completedTasksByUser[toDo.userId]) {
          completedTasksByUser[toDo.userId]++;
        } else {
          completedTasksByUser[toDo.userId] = 1;
        }
      }
    });

    Object.entries(completedTasksByUser).forEach(([userId, count]) => {
      console.log(`User Id: ${userId}, Completed Tasks: ${count}`);
    });
  }
});
