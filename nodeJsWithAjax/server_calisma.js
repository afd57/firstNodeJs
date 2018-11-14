var express = require('express');
var app = express();
var path = require('path')

app.set('view engine', 'ejs');



app.get('/',function(req,res){
    console.log(path.join(__dirname, 'css'));
    //res.send('<h1>Hello :P</h1>');
    app.use(express.static(path.join(__dirname, 'css')));
    app.use(express.static(path.join(__dirname, 'js')));

    res.sendFile(__dirname + '/index.html')

});

app.get("/contact/:name", function(req,res) {

 res.send(req.params)

});

 app.get("/about", function(req,res) {

  res.send(req.query); // ?user=kenan

 });

app.listen(8000,function(){
console.log("Server started! port:8000");
});