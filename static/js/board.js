document.addEventListener('DOMContentLoaded', () => {
    console.log('Board ready');
    loadMessages();
});

const messageBoard = document.getElementById('message-board');

let page = 1;
let loading = false;

createMessageElement = (message) => {
  const div = document.createElement('div');
  div.classList.add('message');
  
  const title = document.createElement('h2');
  title.classList.add('message-title');
  title.innerText = message.title;
  div.appendChild(title);
  
  const text = document.createElement('p');
  text.classList.add('message-text');
  text.innerText = message.text;
  div.appendChild(text);

    const time = document.createElement('p');
    time.classList.add('message-time');
    time.innerText = message.time;
    div.appendChild(time);
  
  return div;
}

get_cookie = (name) => {
    let value = "; " + document.cookie;
    let parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

postMessage = async() => {
    const title = document.getElementById('message-title').value;
    const text = document.getElementById('message-text').value;
    let time = moment().format('YYYY-MM-DD HH:mm:ss');
    if(title == "" || text == ""){
        console.log("post_message_error, empty title or text");
        return;
    }
    const options = {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'X-CSRF-TOKEN': get_cookie('csrf_access_token'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"title": title, "text": text, "time": time})
    };
    console.log("post_message ing")
    const response = await fetch('/api/board/', options)
    const result = await response.json();
    if(result.status == "0"){
        console.log("post_message_ok");
        const message = { title: title, text: text , time: time};
        const messageElement = createMessageElement(message);
        messageBoard.insertBefore(messageElement, messageBoard.firstChild);
        document.getElementById('message-title').value = '';
        document.getElementById('message-text').value = '';
        return;
    }
    console.log("post_message_error");
}






window.addEventListener('scroll', () => {
  if (window.innerHeight + window.scrollY >= document.body.scrollHeight) {
    loadMessages();
  }
});



// load messages on DOM ready, 5 at a time
loadMessages = async() => {
    if (loading) return;
    loading = true;
    const options = {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': get_cookie('csrf_access_token')
        }
    };

    const response = await fetch(`/api/board/?page=${page}`, options);
    const messages = await response.json();
    console.log(messages);
    data = messages.messages;
    console.log(data);
    // messages.forEach(message => {
    //     const messageElement = createMessageElement(message);
    //     messageBoard.appendChild(messageElement);
    // });
    for (let i = 0; i < data.length; i++) {
        const messageElement = createMessageElement(data[i]);
        // newest is on top
        // messageBoard.appendChild(messageElement);
        messageBoard.insertBefore(messageElement, messageBoard.firstChild);
    }
    page++;
    loading = false;
}
