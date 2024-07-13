const net = require('net');

const clients = [];

const broadcast = (message, sender) => {
    clients.forEach((client) => {
        if (client !== sender) {
            client.write(message);
        }
    });
};

const server = net.createServer((socket) => {
    clients.push(socket);
    console.log('New client connected');
    
    socket.on('data', (data) => {
        console.log('Received: ' + data.toString());
        broadcast(data, socket);
    });

    socket.on('end', () => {
        console.log('Client disconnected');
        clients.splice(clients.indexOf(socket), 1);
    });

    socket.on('error', (err) => {
        console.error(err);
    });
});

server.listen(65432, '127.0.0.1', () => {
    console.log('Server listening on 127.0.0.1:65432');
});
