//author - Animcogn
//purpose - host google maps server
//created - 1/8/2018
//last edit - 1/8/2018

var express = require('express');
var app = express();

app.use(express.static('public'));

app.get('/database', function(req, res) {
    const sqlite3 = require('sqlite3').verbose();

    // open the database
    let db = new sqlite3.Database('./suspicious_devices.db');

    let sql = 'SELECT * FROM devices WHERE threat_rating >= 1'; //<--- adjust this for false alarms

    db.all(sql, [], (err, rows) => {
      if (err) {
        throw err;
      }
     rows.forEach((row) => {
        console.log(JSON.stringify(row));
      });

    res.send(rows);
    // close the database connection
    db.close();
    });
});

var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port

   console.log("Example app listening at http://%s:%s", host, port)
})
