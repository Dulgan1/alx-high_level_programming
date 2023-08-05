// Gets hello data and use as text in div with hello class
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function () {
      $(div#hello).text(data.hello);
    }
  });
});
