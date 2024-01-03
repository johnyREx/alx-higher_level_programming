#!/usr/bin/node
/* 8 (adv). Return list of names of characters from movie in order (sync). */

const request = require('request');
const id = process.argv[2];

const url = 'http://swapi.co/api/films/' + id;
const charDict = {};

// get list of characters
request.get(url, (err, response, body) => {
  if (err) throw err;
  const charList = JSON.parse(body).characters;
  let count = 0;
  // go through list and querry each url
  for (let i = 0; i < charList.length; i++) {
    request.get(charList[i], (err, response, body) => {
      if (err) throw err;
      // save each result and pull out url(key) and name(value) for dict.
      const person = JSON.parse(body);
      charDict[person.url] = person.name;
      count++;
      // once all are pulled and stored, go through dict and log results
      if (count === charList.length) {
        for (const charURL of charList) {
          console.log(charDict[charURL]);
        }
      }
      // console.log(JSON.parse(body).name); // debug
      // console.log(charDict); // debug
    });
  }
});
