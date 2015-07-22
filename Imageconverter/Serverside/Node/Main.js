
var express = require('express');
var app = express();
var path = require('path');
var readline = require('readline');



//app.use(express.compress()); ## option for compressing with gzip
app.use(express.static(path.join(__dirname, '../../Website'))); // tells express where to look for the static files
app.listen(process.env.PORT || 1706);


console.log('Server running at http://127.0.0.1:1706/');
