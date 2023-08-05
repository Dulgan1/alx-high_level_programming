// Fetches and lists all movie titles from api
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: functioon (data) {
      const titles = data.results;
      for (const t in titles) {
        $('ul#list_movies').append('<li>' + titles[i].title + '<li>');
      }
    }
  });
});
