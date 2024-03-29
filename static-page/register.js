document.getElementById("register-button").addEventListener("click", async function(event) {
    event.preventDefault();
    const email = document.getElementById("email").value;
    const passwordEnter = document.getElementById("password-enter").value;
    const passwordVerify = document.getElementById("password-verify").value;
    if (passwordEnter == passwordVerify) {
        await register(email, passwordVerify);
    }
    else {
        document.getElementById("register-error").innerText = "Passwords do not match! Try again."
    }

});

async function register(email, password) {
    await fetch(
        "https://autoresumed.com/api/auth/register",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "email": email, "password": password })
        }
    );
}
