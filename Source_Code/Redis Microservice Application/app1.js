// Importing 'express' web framework and 'redis' client
const express_framework = require('express');
const redis_db = require('redis');

// Creating a redis client
const client_create = redis_db.createClient({host:'localhost', port: 6379});

// Checking the connection to redis client
client_create.on('error', (catch_err) => {
    console.log('Error occured while connecting to redis client. Error Details: ', catch_err);
});

client_create.on('connect', () => {
    console.log('Successfully connected redis client to the server');
});

// Creating the microservice application to interact with redis
const my_microservice_app = express_framework();

// Creating endpoint to set key-value pair in Redis
my_microservice_app.post('/set', (request, response) => {
    client_create.set('testKey', 'testValue', (error, rep) => {
        if (error) {
            console.error(error);
            response.status(500).send('Error occured while setting the key');
            return;
        }
        response.send('Key and Value set successfully');
    });
});

// Creating endpoint to get value from Redis
my_microservice_app.get('/get', (request, response) => {
    client_create.get('testKey', (error, rep) => {
        if (error) {
            console.error(error);
            response.status(500).send('Error occured while getting the key');
            return;
        }
        response.send(`Value: ${rep}`);
    });
});

const PORT = process.env.PORT || 3000;
my_microservice_app.listen(PORT, () => {
    console.log(`Server is now running on port ${PORT}`);
});
