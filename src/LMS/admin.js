document.getElementById("loginForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("error-message");

    // Perform client-side validation (replace this with server-side validation in a real app)
    if (username === "" || password === "") {
        errorMessage.textContent = "Please enter both username and password.";
    } else if (username !== "admin" || password !== "password") {
        errorMessage.textContent = "Invalid username or password.";
    } else {
        // Simulate successful login (replace with server-side authentication)
        alert("Login successful!");
        errorMessage.textContent = "";
    }
});
