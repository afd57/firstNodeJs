var express = require('express');
var app = express();
var fs = require('fs');
var obj;

app.get('/download', function(req, res){
    var file = __dirname + '/upload_folder/htmldiff.zip';
    res.download(file); // Set disposition and send it.
  });
  
app.listen(8000,function(){
    console.log('Example App listening on port 8000');
});