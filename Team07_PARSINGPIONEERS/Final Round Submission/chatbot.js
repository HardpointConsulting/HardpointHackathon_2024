document.querySelector('.send-btn').addEventListener('click', function() {
    var input = document.querySelector('.chat-input');
    var message = input.value;
    if (message) {
        var messagesContainer = document.querySelector('.messages');
        
        // Create new message container
        var messageContainer = document.createElement('div');
        messageContainer.classList.add('message-container');

        // Create new message element for user
        var userMessageElement = document.createElement('div');
        userMessageElement.classList.add('user-message');
        userMessageElement.textContent = message;

        // Append user message to message container
        messageContainer.appendChild(userMessageElement);

        // Append message container to messages container
        messagesContainer.appendChild(messageContainer);
        
        // Simulate a chatbot response
        setTimeout(() => {
            // Create new message element for chatbot response
            var chatbotResponseElement = document.createElement('div');
            chatbotResponseElement.classList.add('chatbot-response');
            chatbotResponseElement.textContent = 'This is a response from the chatbot.';

            // Append chatbot response to message container
            messageContainer.appendChild(chatbotResponseElement);

            // Scroll to bottom of messages container
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }, 1000);
        
        input.value = ''; // Clear input field
    }
    
});
