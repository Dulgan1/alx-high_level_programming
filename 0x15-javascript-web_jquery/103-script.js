//
document.addEventListener('DOMContentLoaded', function () {
  $('input#btn_translate').click(function () {
    complete();
  });
  $('input#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      complete();
    }
  });
  function complete () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=';
    const l = $('input#language_code').val();
    $.ajax({
      type: 'GET',
      url: `${url}${l}`,
      success: function (data) {
        $('div#hello').text(data.hello);
      }
    });
  }
});
