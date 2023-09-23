document.getElementById("registrationForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const firstname = document.getElementById("firstname").value;
    const lastname = document.getElementById("lastname").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const mobileNumber = document.getElementById("mobileNumber").value;
    const email = document.getElementById("email").value; 
    const errorMessage = document.getElementById("error-message");

    // Perform client-side validation (replace this with server-side validation in a real app)
    if (firstname === "" || lastname === "" || username === "" || password === "" || mobileNumber === "" || email === "") {
        errorMessage.textContent = "Please enter both username and password.";
    } else if (username.length < 3 || password.length < 6) {
        errorMessage.textContent = "Username should be at least 3 characters long, and password should be at least 6 characters long.";
    } else {
        // Simulate successful registration (replace with server-side registration logic)
        alert("Registration successful!");
        errorMessage.textContent = "";
        // Redirect to the login page
        window.location.href = "admin.html";
    }
});
