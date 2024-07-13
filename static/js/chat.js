document.addEventListener('DOMContentLoaded', () => {
    console.log('Chat initializing...');
    let socket = io();
            socket.on('connect', function() {
                console.log('WebSocket connected!');
                socket.send('User has connected!');
            });

            socket.on('system-response', (data) => {
                console.log(data["data"]);
            });

            socket.on('message', function(msg) {
                console.log('Received message: ' + msg);
            });

            // document.getElementById('send-button').onclick = function() {
            //     // socket.send(document.getElementById('message-input').value);
            //     socket.emit("message",{
            //         // user: get_cookie('username'),
            //         // message: document.getElementById('message-input').value,
            //         // time: moment().format('YYYYMMDDHHmmss')
            //         data: document.getElementById('message-input').value
            //     })
            // };
            socket.emit("system",{
                // user: get_cookie('username'),
                // message: document.getElementById('message-input').value,
                // time: moment().format('YYYYMMDDHHmmss')
                data: "websocket OK"
            })
});

