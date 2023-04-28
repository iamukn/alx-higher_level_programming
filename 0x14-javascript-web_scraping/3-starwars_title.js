#!/usr/bin/node
// API digest
// Author: IAM_UKN

// Receives argument from the command line
const id = process.argv[2];

// Append the argument to the url to retrieve the Movie info using the id
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// import the request module
const request = require('request');

// make an api call to the url using the request instance created
request(url, (err, response, body) => {
// test to see if there's a response from the api
  if (response) {
    // convert the JSON object received to a Javascript object
    const res = JSON.parse(body);
    // print the title of the movie using the dot or bracket notation
    console.log(res.title);
  }
  // Error handling
  if (err) {
    // print the error to the console if caught
    console.log(err);
  }
});
