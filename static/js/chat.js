const socket = io()
let isMe = false;

scrollToBottom = () => {
    const chatMessages = document.getElementById("chat-messages");
    chatMessages.scrollTop = chatMessages.scrollHeight;
}



// https://socket.io/docs/v4/client-api/#event-connect

//看著文件寫 拜託~
document.addEventListener('DOMContentLoaded', () => {
    console.log('Chat initializing...');
            socket.on('connect', () => {
                socket.send('User has connected!');
            });

            //主動 websocket 需求 取得目前聊天資料
            socket.emit("system",{
                // time: moment().format('YYYYMMDDHHmmss')
                data: "Websocket Connected"
            })
            //接聽上方提出需求之回應 並將聊天資料製作 message
            socket.on('system-response', (data) => {
                console.log(data["data"]);
                messageMaker(data)
            });

            //接聽來自伺服器單一最新訊息 並製作 message
            socket.on('messager_recieve', (data) => {
                console.log("!here!")
                console.log('Received message: ' + data.msg);
                messageMaker(data)
            });

            // 空訊息 測試 socket 是否需要一次的訊息後才能使用
            socket.emit("messager_send",{
                msg: "test_123"
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


    // if socket.connected?? add?
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
        data.message.forEach((msg) => {
            const div = document.createElement('div');
            const p = document.createElement('p');
            if (data.type == "system") {
                console.log("is system", msg);
                div.classList.add('chat-system');
                p.textContent = msg;
                div.appendChild(p);
            } else {
                if (whoAmI == msg.who){
                    isMe = true;
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
