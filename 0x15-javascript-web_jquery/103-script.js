#!/usr/bin/node
const $ = window.$;

$(function() {
  $('INPUT#btn_translate, INPUT#language_code').on('click keypress', function(data) {
    if (data.type === 'click' || (data.type === 'keypress' && data.which === 13)) {
      const languageCode = $('INPUT#language_code').val();
      const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}';
      
      $.get(url, function(greet) {
        $('DIV#hello').text(greet.hello);
      });
    }
  });
});
