#!/usr/bin/node
// html elemnt with red color

$('#red_header').bind('click', function () {
  $('header').attr('class', 'red');
});
