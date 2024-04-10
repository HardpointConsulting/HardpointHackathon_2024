// JavaScript code to handle login and redirection
document.getElementById('customer-login').addEventListener('click', function() {
    document.getElementById('customer-form').style.display = 'block';
    document.getElementById('employer-form').style.display = 'none';
});

document.getElementById('employer-login').addEventListener('click', function() {
    document.getElementById('employer-form').style.display = 'block';
    document.getElementById('customer-form').style.display = 'none';
});

function submitLogin(userType) {
    // Here you would normally validate the user's credentials via an API call
    // For demonstration purposes, we'll skip the validation and redirect directly

    // Check which user type is logging in and redirect accordingly
    if (userType === 'customer') {
        // Redirect customer to chatbot page
        window.location.href = 'chatbot.html';
    } else if (userType === 'employer') {
        // Redirect employer to chatbot page
        window.location.href = 'chatbot.html';
    }
}