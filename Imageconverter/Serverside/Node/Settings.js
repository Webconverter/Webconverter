var express = require('express');
var readline = require('readline');



//THIS IS THE COMMAND FOR Exeting the app reffered to as quitcommand();
function quitcommand(){
  var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

rl.question("Are you sure you want to quit y/n\n", function(exit){
  if(exit = ('y'))
  {
    process.exit(code=0)
  }
});
}
module.exports.quit = quitcommand();
