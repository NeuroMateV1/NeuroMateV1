document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = userInput.value.trim();
        if (message === '') return;

        appendMessage(message, 'user');
        userInput.value = '';

        callAgent(message);
    }

    function appendMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', sender);
        messageElement.textContent = message;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    async function callAgent(userMessage) {
        appendMessage('...', 'agent'); // Show a typing indicator
        try {
            const endpoint = 'http://localhost:5000/predict'; // Backend proxy endpoint
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: userMessage, // Send message to backend
                }),
            });

            const data = await response.json();
            const agentResponse = data.response; // Get response from backend

            chatMessages.removeChild(chatMessages.lastChild); // Remove typing indicator
            appendMessage(agentResponse, 'agent');
        } catch (error) {
            console.error('Error calling agent:', error);
            chatMessages.removeChild(chatMessages.lastChild); // Remove typing indicator
            appendMessage('Error: Could not connect to the agent.', 'agent');
        }
    }
}); 