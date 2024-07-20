
const socket = io()
document.addEventListener('DOMContentLoaded', () => {
    console.log('Chat initializing...');
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

            document.getElementById('send-button').addEventListener('click', sendMessage);
            document.getElementById('message-input').addEventListener('keyup', function(event) {
                if (event.key === 'Enter') {
                    sendMessage();
                }
            });

            
});


sendMessage = () => {
    console.log("sending msg")
    let message = document.getElementById('message-input').value;
    socket.emit("message",{
        // user: get_cookie('username'),
        // message: document.getElementById('message-input').value,
        // time: moment().format('YYYYMMDDHHmmss')
        data: message
    })
    document.getElementById('message-input').value = '';
};