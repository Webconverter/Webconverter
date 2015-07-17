
var express = require('express');
var app = express();
var path = require('path');

console.log(path.join(__dirname, '../../Website/'));
app.use(express.static(path.join(__dirname, '../../Website')));
app.listen(process.env.PORT || 3000);

console.log('Server running at http://127.0.0.1:1706/');
