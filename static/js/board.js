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
    div.id = `message-${message.id}`;

    const message_top = document.createElement('div');
    message_top.classList.add('message-top');
    
    const title = document.createElement('h2');
    title.classList.add('message-title');
    title.innerText = message.title;
    message_top.appendChild(title);

    const delete_btn = document.createElement('button');
    delete_btn.classList.add('delete-btn');
    delete_btn.innerText = 'x';
    delete_btn.addEventListener('click', () => {
        deleteMessage(message.id);
    });
    message_top.appendChild(delete_btn);

    div.appendChild(message_top);

    const text = document.createElement('p');
    text.classList.add('message-text');
    text.innerText = message.content;
    div.appendChild(text);

    const time = document.createElement('p');
    time.classList.add('message-time');
    console.log(message);
    // time.innerText = message.time; 暫時 之後要改掉!
    // time.innerText = moment(message.timestamp, "YYYYMMDDHHmmss").format("YYYY-MM-DD HH:mm:ss");
    time.innerText = message.timestamp
    div.appendChild(time);

    if(message.image_id){
        const image = document.createElement('img');
        image.classList.add('message-image');
        image.src = "https://images.pikxl.link/"+message.image_id;
        div.appendChild(image);
    }
  
  return div;
}

get_cookie = (name) => {
    let value = "; " + document.cookie;
    let parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

postMessage = async() => {
    const title = document.getElementById('message-title').value;
    const content = document.getElementById('message-text').value;
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];
    const formData = new FormData();
    let image_id;
    let options;
    let time = moment().format('YYYYMMDDHHmmss');

    if(title == "" || content == ""){
        console.log("post_message_error, empty title or text");
        return;
    }

    formData.append('file', file);
    formData.append('data', JSON.stringify({"title": title, "content": content, "time": time}));
    options = {
        method: 'POST',
        body: formData,
        headers: {
            // 'Authorization': 'Bearer '+ get_cookie('token'),
            'X-CSRF-TOKEN': get_cookie('csrf_access_token')
            // 'Content-Type':'multipart/form-data'
        }
    }


    const response = await fetch('/api/board/', options)
    const result = await response.json();
    //這裡要接回ID

    if(result.status == "0"){
        console.log(result)
        const message = { title: title, content: content , timestamp: time, id:result.id ,image_id:result.image_id};
        const messageElement = createMessageElement(message);
        messageBoard.insertBefore(messageElement, messageBoard.firstChild);
        document.getElementById('message-title').value = '';
        document.getElementById('message-text').value = '';
        if(file){
            file = "";
        }
        return;
    }else{
        console.log("post_message_error");
        file = "";
    }

}





window.addEventListener('scroll', () => {
  if (window.innerHeight + window.scrollY >= document.body.scrollHeight) {
    loadMessages();
  }
});



// load messages on DOM ready, 5 at a time
loadMessages = async(currentPage) => {
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
    if(messages.status!=0) return;
    data = messages.messages;
    //按照 timestamp 排序
    data.sort((a,b) => a.comment_id - b.comment_id)

    // messages.forEach(message => {
    //     const messageElement = createMessageElement(message);
    //     messageBoard.appendChild(messageElement);
    // });
    for (let i = 0; i < data.length; i++) {
        const messageElement = createMessageElement(data[i]);
        // newest is on top
        messageBoard.appendChild(messageElement);
        // messageBoard.insertBefore(messageElement, messageBoard.firstChild);
    }
    page++;
    loading = false;
}

deleteMessage = async(comment_id) => {
    const options = {
        method: 'DELETE',
        credentials: 'same-origin',
        headers: {
            'X-CSRF-TOKEN': get_cookie('csrf_access_token'),
            'Content-Type': 'application/json'
        }
    };

    const response = await fetch(`/api/board/?comment_id=${comment_id}`, options);
    const result = await response.json();
    console.log(result);
    if(result.status == "0"){
        console.log("delete_message_ok");
        const messageElement = document.getElementById(`message-${comment_id}`);
        messageBoard.removeChild(messageElement);
        return;
    }
    console.log("delete_message_error");
}


// infinite scrolling
messageBoard.addEventListener('scroll', (e) => {
    if (loading){
        console.log("scrolling, but already loading");
        return
    };
    const scrollTop = e.target.scrollTop;
    const scrollHeight = e.target.scrollHeight;
    const clientHeight = e.target.clientHeight;

    if (scrollTop + clientHeight >= scrollHeight - 200) {
        console.log("scrolling, now fetching page:", page);
        loading = true;
        loadMessages(page);
    }
})