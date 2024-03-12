document.getElementById("registerForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    await register(email, password);
});

async function register(email, password) {
    await fetch(
        "http://127.0.0.1:5000/auth/register",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "email": email, "password": password })
        }
    );
}
