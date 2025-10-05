const express = require('express');
const { console } = require('inspector');
const app = express();
const port = 3000;

const language = 'NodeJS';

app.get('/', (req, res) => {
    res.send(`<h1>Hello World from {language}</h1>`);
});

app.get('/language', (req, res) => {
    res.json({
        language: language
    });
});

app.listen(port, () => {
    console.log(`Express Server is ready! Port: ${port}`);
});
