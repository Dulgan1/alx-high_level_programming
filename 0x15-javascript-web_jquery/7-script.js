// Gets name and place name text in div with class character.
$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json'
    success: (data) => {
      $('div#character').text(data.name);
    }
  });
});
