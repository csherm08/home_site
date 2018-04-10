var express = require('express');
var server = express();
var fs = require("fs");

const FILENAME = 'lightSwitchBool.txt';
const port = 8000;

server.get('/switchStatus', function (req, res) {
    fs.readFile(FILENAME, 'utf8', function (err, data) {
        console.log(data);
        res.end(data);
    })
})

server.post('/switchStatus', async function (req, res) {

    const fileContents = fs.readFileSync(FILENAME, 'utf8');
    console.log(fileContents);
    let switchBool = fileContents == 'true';
    switchBool = (!switchBool).toString();

    fs.writeFileSync(FILENAME, switchBool);
    res.send(switchBool);
})

var server = server.listen(port, function () {

    var host = server.address().address
    var port = server.address().port
    console.log("Example server listening at %s", port)

})
