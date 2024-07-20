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
  //set ID
  div.id = `message-${message.comment_id}`;

  const message_top = document.createElement('div');
  //把格式放好
  
  const title = document.createElement('h2');
  title.classList.add('message-title');
  title.innerText = message.title;
  div.appendChild(title);

  const delete_btn = document.createElement('button');
  delete_btn.classList.add('delete-btn');
  delete_btn.innerText = 'X';
  delete_btn.addEventListener('click', () => {
    deleteMessage(message.comment_id);
  });
  div.appendChild(delete_btn);
  
  const text = document.createElement('p');
  text.classList.add('message-text');
  text.innerText = message.text;
  div.appendChild(text);

    const time = document.createElement('p');
    time.classList.add('message-time');
    console.log(message);
    // time.innerText = message.time; 暫時 之後要改掉!
    time.innerText = moment(message.comment_id, "YYYYMMDDHHmmss").format("YYYY-MM-DD HH:mm:ss");
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
    let time = moment().format('YYYYMMDDHHmmss');
    if(title == "" || text == ""){
        console.log("post_message_error, empty title or text");
        return;
    }

    //Image upload is here
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('/api/board/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        if (result.success) {
            console.log("image upload success")
        } else {
            console.log("image upload failed")
        }
    } else {
        console.log("no img need to upload")
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
        const message = { title: title, text: text , comment_id: time };
        const messageElement = createMessageElement(message);
        messageBoard.insertBefore(messageElement, messageBoard.firstChild);
        document.getElementById('message-title').value = '';
        document.getElementById('message-text').value = '';
        fileInput.remove();
        return;
    }else{
        console.log("post_message_error");
        fileInput.remove();
    }
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
    //按照 timestamp 排序
    data.sort((a,b) => a.comment_id - b.comment_id)

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


//board img Uploader

// document.getElementById('upload-button').addEventListener('click', async () => {
//     const fileInput = document.getElementById('file-input');
//     const file = fileInput.files[0];
//     if (file) {
//         const formData = new FormData();
//         formData.append('file', file);

//         const response = await fetch('/api/board/upload', {
//             method: 'POST',
//             body: formData
//         });

//         const result = await response.json();
//         if (result.success) {
//             alert('File uploaded successfully');
//         } else {
//             alert('File upload failed');
//         }
//     } else {
//         alert('Please select a file to upload');
//     }
// });