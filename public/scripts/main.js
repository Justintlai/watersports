$(document).ready(function() {
  $('button').click(getData);

  function getData() {
    var topic = $('#topic').val();
    var skipNum = $('#skipNum').val();

    $.ajax({
      url: 'http://192.168.1.67:5000',
      data: $('form').serialize(),
      beforeSend: function() {
        // this is where we append a loading image
        $('#ajax-panel').html(
          '<div class="loading"><img src="/img/loading.gif" alt="Loading..." /></div>'
        );
      },
      type: 'POST',
      timeout: 2000,
      success: function(result) {
        console.log(result);
        $('#ajax-panel').empty();
        for (var i = 0; i < result.length; i++) {
          $('#result').append(result[i].link_text + '</br>');
          $('#result').append(
            '<a href=' + result[i].link + '>Source<a>' + '</br>'
          );
          $('#result').append(new Date(result[i].time * 1000) + '</br>');
          $('#result').append(result[i].source + '</br>');
          $('#result').append('</br></br>');
        }
      },
      error: function(error) {
        console.log(error);
        // failed request; give feedback to user
        $('#ajax-panel').html(
          '<p class="error"><strong>Oops!</strong> Try that again in a few moments.</p>'
        );
      }
    });
  }

  $(window).scroll(function() {
    if ($(window).scrollTop() == $(document).height() - $(window).height()) {
      // ajax call get data from server and append to the div
      getData();
    }
  });
});
