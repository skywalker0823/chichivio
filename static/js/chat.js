// 宣告變數
let name = '';
let socket = null;
let chatlog = document.getElementById('chatlog');
let messageInput = document.getElementById('message-input');

// 加入聊天室按鈕
document.getElementById('join-button').addEventListener('click', () => {
	// 取得使用者名稱
	_name = document.getElementById('name-input').value.trim();
	if (_name === '') {
		alert('請輸入名稱');
		return;
	}

	// 連接到 WebSocket 伺服器
	socket = new WebSocket('ws://localhost:3000');

	// 連接成功後，顯示聊天室介面
	socket.addEventListener('open', () => {
		document.querySelector('.header').classList.add('hidden');
		document.querySelector('.chatroom').classList.remove('hidden');
	});

	// 接收訊息
	socket.addEventListener('message', event => {
		let data = JSON.parse(event.data);
        let message = document.createElement('div');
        message.classList.add('message');
        message.innerHTML = `<div class="message__name">${data.name}</div><div class="message__text">${data.text}</div>`;
        chatlog.appendChild(message);

        // 捲動到最下方
        chatlog.scrollTop = chatlog.scrollHeight;

        // 清空輸入框
        messageInput.value = '';

        // 聚焦輸入框
        messageInput.focus();

        // 顯示訊息
        message.classList.add('message--show');

        // 顯示訊息
        message.classList.add('message--show');
    });

    // 關閉連線
    socket.addEventListener('close', () => {
        document.querySelector('.header').classList.remove('hidden');
        document.querySelector('.chatroom').classList.add('hidden');
    });
});





