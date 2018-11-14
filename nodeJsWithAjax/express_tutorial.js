var express = require('express');
var app = express();

app.use(express.static('public'));
app.get('/',function(req, res){
    res.sendFile(__dirname + '/index.html')
});

var index=0;
app.get('/theURL',function(req, res){    
    index++;
    res.send(index.toString())
});
app.listen(8000,function(){
    console.log('Example App listening on port 8000');
});