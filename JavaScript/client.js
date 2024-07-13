const net = require('net');
const readline = require('readline');

const client = new net.Socket();
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

client.connect(65432, '127.0.0.1', () => {
    console.log('Connected to the server');
});

client.on('data', (data) => {
    console.log('Received: ' + data.toString());
});

client.on('close', () => {
    console.log('Connection closed');
});

rl.on('line', (input) => {
    client.write(input);
});
