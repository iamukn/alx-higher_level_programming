#!/usr/bin/node

$('Document').ready(() => {
  $('#update_header').click(update);
  function update () {
    $('header').text('New Header');
  }
});
