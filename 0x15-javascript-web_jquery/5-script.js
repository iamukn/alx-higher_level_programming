#!/usr/bin/node

$('Document').ready(() => {
  $('#add_item').click(add);
  function add () {
    $('ul.my_list').append('<li>Item</li>');
  }
});
