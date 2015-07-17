
var http = require('http');
var fs = require('fs');

http.createServer(function (request, response) {
    console.log('request starting...');
    response.writeHead(200,{'Content-Type': 'text/plain'});
    response.end('hello');
}).listen(1706, '127.0.0.1');
console.log('Server running at http://127.0.0.1:1706/');
