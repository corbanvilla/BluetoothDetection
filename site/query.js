const sqlite3 = require('sqlite3').verbose();

// open the database
let db = new sqlite3.Database('./suspicious_devices.db');

let sql = 'SELECT * FROM devices WHERE threat_rating >= 1';

db.all(sql, [], (err, rows) => {
  if (err) {
    throw err;
  }
  rows.forEach((row) => {
    console.log(row);
  });
});

// close the database connection
db.close();
