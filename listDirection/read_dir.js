var fs = require('fs');
var express = require('express');
var app = express();
var obj;
 
var path2 = '/Users/mbp13/Desktop/git_project';
 
function walk(currentDirPath, callback) {
    var fs = require('fs'),
        path = require('path');
    fs.readdir(currentDirPath, function (err, files) {
        if (err) {
            throw new Error(err);
        }
        files.forEach(function (name) {
            var filePath = path.join(currentDirPath, name);
            var stat = fs.statSync(filePath);
            if (stat.isFile()) {
                callback(filePath, stat);
            } else if (stat.isDirectory()) {
                walk(filePath, callback);
            }
        });
    });
}



app.listen(8000,function(){
    console.log('Example App listening on port 8000');
    walk(path2, function(filePath, stat) {
        console.log(filePath)
    });
});