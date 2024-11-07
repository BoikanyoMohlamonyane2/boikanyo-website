document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("chat-form");
    const messages = document.getElementById("chat-messages");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        // Get the user input
        const name = form.querySelector('[name="name"]').value;
        const email = form.querySelector('[name="email"]').value;
        const message = form.querySelector('[name="message"]').value;

        // Display the message in the chatbox
        const userMessage = document.createElement("div");
        userMessage.classList.add("user-message");
        userMessage.innerHTML = `<strong>${name}</strong>: ${message}`;
        messages.appendChild(userMessage);

        // Scroll to the bottom of the chatbox
        messages.scrollTop = messages.scrollHeight;

        // Submit the form to send the email
        form.submit();
    });
});
