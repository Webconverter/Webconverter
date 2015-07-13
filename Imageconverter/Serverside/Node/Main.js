
var http = require('http');
var fs = require('fs');
http.createServer(function (request, response) {
    console.log('request starting...');

	fs.readFile('./Website\index.html', function(error, content) {
		if (error) {
			response.writeHead(500);
      console.log('error');
			response.end();
		}
		else {
			response.writeHead(200, { 'Content-Type': 'text/html' });
			response.end(content, 'utf-8');
      console.log("sucsess");
		}
	});

}).listen(8125);
console.log('Server running at http://127.0.0.1:8125/');
