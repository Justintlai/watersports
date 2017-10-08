var http = require('http'),
  express = require('express'),
  parser = require('body-parser');

// Setup express
// Setup an App with express, configure app to use body parser and assign port to our app.
var app = express();
app.use(parser.json());
app.use(parser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/public'));
app.set('view engine', 'ejs');
app.set('port', process.env.PORT || 5000);

// Set default route
app.get('/', function(req, res) {
  res.render('landing');
});

// Create server
// Create server that will listen specified port that we defined earlier.
http.createServer(app).listen(app.get('port'), function() {
  console.log('Server listening on port ' + app.get('port'));
});
