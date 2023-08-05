// 
document.addEventListener('DOMContentLoaded', function () {
  $('input#btn_translate').click(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    const l = $('input#language_code').val();
    $.ajax({
      type: 'GET',
      url: `${url}${l}`,
      success: function (data) {
        $('div#hello').text(data.hello);
      }
    });
  });
});
