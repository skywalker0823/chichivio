const socket = io()
let isMe = false;

scrollToBottom = () => {
    const chatMessages = document.getElementById("chat-messages");
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('Chat initializing...');
            socket.on('connect', () => {
                console.log('WebSocket connected!');
                socket.send('User has connected!');
            });

            socket.on('system-response', (data) => {
                console.log(data["data"]);
                messageMaker(data)
            });

            socket.on('messager_recieve', (data) => {
                console.log("!here!")
                console.log('Received message: ' + data.msg);

                messageMaker(data)

            });

            socket.emit("system",{
                // time: moment().format('YYYYMMDDHHmmss')
                data: "Websocket Connected"
            })

            document.getElementById('send-button').addEventListener('click', sendMessage);
            document.getElementById('message-input').addEventListener('keyup', function(event) {
                if (event.key === 'Enter') {
                    sendMessage();
                }
            });     
});


sendMessage = () => {
    isMe = true;
    console.log("sending msg")
    let message = document.getElementById('message-input').value;
    socket.emit("messager_send",{
        // time: moment().format('YYYYMMDDHHmmss')
        msg: message
    })
    document.getElementById('message-input').value = '';
};

messageMaker = (data) => {
    console.log(data, typeof data)
    const chatMessages = document.getElementById("chat-messages");
    const whoAmI = data.you
    console.log(whoAmI)

    // 檢查 message 是否為陣列, 通常為 reload action
    if (Array.isArray(data.message)) {
        // 如果是陣列，遍歷每條訊息
        console.log(data.message, typeof data.message)
        data.message.forEach((msg) => {
            const div = document.createElement('div');
            const p = document.createElement('p');
            console.log(msg,typeof msg)
            //convert string to dict
            // 根據訊息的 type 判斷顯示樣式
            if (data.type == "system") {
                console.log("is system", msg);
                div.classList.add('chat-system');
                p.textContent = msg;
                div.appendChild(p);
            } else {
                if (whoAmI == msg.who){
                    isMe = true;
                    console.log("is me");
                    div.classList.add('chat-me');
                    p.textContent = msg.who+":"+msg.msg;
                    div.appendChild(p)
                }
                else {
                    console.log("is other");
                    div.classList.add('chat-other');
                    p.textContent = msg.who+":"+msg.msg;
                    div.appendChild(p)
                }
            }

            chatMessages.appendChild(div);
        });
        //單一訊息收發
    } else {
        const div = document.createElement('div');
        const p = document.createElement('p');
        let message = data.message;
        let who = data.who;
        let type = data.type;

        if (isMe){
            console.log("is me");
            div.classList.add('chat-me');
            p.textContent = data.who+":"+data.msg;
            div.appendChild(p)
        }
        else {
            console.log("is other");
            div.classList.add('chat-other');
            p.textContent = data.who+":"+data.msg;
            div.appendChild(p)
        }

        chatMessages.appendChild(div);
    }
    scrollToBottom();
    isMe = false;
};
