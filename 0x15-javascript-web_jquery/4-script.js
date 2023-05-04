#!/usr/bin/node

$('Document').ready(() => {
  $('#toggle_header').click(toggle);

  function toggle () {
    if ($('#toggle_headeer').hasClass('red')) {
      $('#toggle_header').removeClass('red');
      $('#toggle_header').addClass('green');
    } else if ($('#toggle_headeer').hasClass('green')) {
      $('#toggle_header').removeClass('green');
      $('#toggle_header').addClass('red');
    } else {
      $('#toggle_header').addClass('green');
    }
  }
});
