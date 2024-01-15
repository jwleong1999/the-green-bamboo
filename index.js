// var Express = require("express");
// var MongoClient = require('mongodb').MongoClient;
// var cors = require('cors');
// const multer = require('multer');

// var app = Express();
// app.use(cors());

// var connection_string = `mongodb+srv://jwleong2020:uOfXCrxLPCjgyA92@greenbamboo.wbiambw.mongodb.net/?retryWrites=true&w=majority`
// var database_name = 'GreenBamboo'
// var database;

// // Form database connection
// app.listen (1111, () => {
//     MongoClient.connect(connection_string, (error, client) => {
//         database = client.db(database_name);
//         console.log("Connected to `" + database_name + "`!");
//     });
// });

// // [Producers] Get all producers
// app.get('/api/GetProducers', (request, response) => {
//     database.collection('Producers').find({}).toArray((error, result) => {
//         response.send(result);
//     });
// });
