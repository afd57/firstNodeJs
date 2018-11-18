var express = require('express');
var app = express();
var fs = require('fs');
var obj;

app.use(express.static('public'));
app.get('/',function(req, res){
    res.sendFile(__dirname + '/index.html')
});

var index=0;
app.get('/theURL',function(req, res){
    fs.readFile('test.json', 'utf8', function (err, data) {
        if (err) throw err;
        obj = JSON.parse(data);
        res.setHeader('Content-Type', 'application/json');
        res.send(JSON.stringify(obj));
        console.log(obj);
      });

    
    
});
app.listen(8000,function(){
    console.log('Example App listening on port 8000');
});