#!/usr/bin/node
/* 7 (adv). take movie id arg and return names of all characters in movie. */

const request = require('request');
const id = process.argv[2];

const url = 'http://swapi.co/api/films/' + id;

// get list of characters
request.get(url, (err, response, body) => {
  if (err) throw err;
  const charList = JSON.parse(body).characters;
  // querry for each URL given to get character name
  for (let i = 0; i < charList.length; i++) {
    request.get(charList[i], (error, response, body) => {
      if (error) throw error;
      console.log(JSON.parse(body).name);
    });
  }
});
