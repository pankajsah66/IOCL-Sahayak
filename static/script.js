const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const typing = document.getElementById('typing');

function appendMessage(text, sender) {
    const div = document.createElement('div');
    div.className = `message ${sender === 'user' ? 'user-msg' : 'bot-msg'}`;
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const msg = userInput.value.trim();
    if (!msg) return;

    appendMessage(msg, 'user');
    userInput.value = '';
    typing.style.display = 'block';

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: msg })
        });
        const data = await response.json();
        
        setTimeout(() => {
            typing.style.display = 'none';
            appendMessage(data.response, 'bot');
        }, 600); // Small delay for realism

    } catch (error) {
        typing.style.display = 'none';
        appendMessage("Connection error. Please try again.", 'bot');
    }
}

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});