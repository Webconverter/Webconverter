
var http = require('http');
var fs = require('fs');
var path = require('path');


fs.readFile(path.join(__dirname, '../../Website/', 'index.html'), function(error, data) {
  //takes a file and a callback function which defines two self explanitory arguments
    if (error) {
      throw error;
    }
    http.createServer(function (request, response) {
      // creates a server and defines request and respnse
      console.log('request starting...');
      // debug message: indicates a when a new request is being made
      response.writeHead(200,{'Content-Type': 'text/html'});
      response.write(data);
      response.end();
    }).listen(1706, '127.0.0.1'); // defines the ip and port to listen to. The local ip is not strictly necessary
});

console.log('Server running at http://127.0.0.1:1706/');
