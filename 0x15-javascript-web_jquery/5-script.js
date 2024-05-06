#!/usr/bin/node
// html elemnt with red color

$('#add_item').bind('click', function () {
    $('.my_list').append('<li>Item</li>');
});
