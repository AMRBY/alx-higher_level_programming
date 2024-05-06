#!/usr/bin/node
// html elemnt with red color

$('#toggle_header').bind('click', function () {
  if ($('header').hasClass('red')) {
    $('header').attr('class', 'green');
  } else {
    $('header').attr('class', 'red');
  }
});
