document.addEventListener('DOMContentLoaded', async() => {
    console.log('Board ready');
});

const messageBoard = document.getElementById('message-board');
const loadMoreButton = document.getElementById('load-more');

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
  
  return div;
}

loadMessages = async() => {
  if (loading) return;
  loading = true;
  
  // const response = await fetch(`https://example.com/messages?page=${page}`);
  // const messages = await response.json();
  const messages = [
    { title: 'Test Message 3', text: 'This is the third test message.' },
    { title: 'Test Message 2', text: 'This is the second test message.' },
    { title: 'Test Message 1', text: 'This is the first test message.' },
  ];
  
  messages.forEach(message => {
    const messageElement = createMessageElement(message);
    messageBoard.insertBefore(messageElement, messageBoard.firstChild);
  });
  
  page++;
  loading = false;
}

loadMoreButton.addEventListener('click', loadMessages);

window.addEventListener('scroll', () => {
  if (window.innerHeight + window.scrollY >= document.body.scrollHeight) {
    loadMessages();
  }
});
