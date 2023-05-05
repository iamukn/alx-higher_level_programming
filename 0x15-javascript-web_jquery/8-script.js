#!/usr/bin/node

$('document').ready(() => {
  const url ='https://swapi-api.alx-tools.com/api/films/?format=json'
  $.get(url, (data, status) => {
    for (let i = 0; i < data['results'].length; i++) {
      $('ul#list_movies').append(`<li>${data['results'][i]['title']}</li>`);
    }
  });
});
