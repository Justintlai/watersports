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
          '<div class="loading"><img class="img-fluid" src="/img/loading.gif" alt="Loading..." /></div>'
        );
      },
      type: 'POST',
      timeout: 2000,
      success: function(result) {
        console.log(result);
        $('#ajax-panel').empty();
        for (var i = 0; i < result.length; i++) {
          $('#result').append(
            '<div class="card">' +
              '<h3 class="card-header">' +
              result[i].source +
              '<div class="card-block"></h3>' +
              '<p class="card-text"><a href=' +
              result[i].link +
              '>Source</a></p>' +
              '<p class="card-text">' +
              new Date(parseInt(result[i].time) * 1000) +
              '</p>' +
              '<p class="card-text">' +
              result[i].link_text +
              '</p>' +
              '</div></div>'
          );
        }
      },

      // <div class="card">
      //   <h3 class="card-header">Featured</h3>
      //   <div class="card-block">
      //     <h4 class="card-title">Special title treatment</h4>
      //     <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
      //     <a href="#" class="btn btn-primary">Go somewhere</a>
      //   </div>
      // </div>

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
