

document.getElementById("registerButton").addEventListener("click", async function(event) {
    event.preventDefault();
    const email = document.getElementById("email").value;
    const passwordEnter = document.getElementById("password-enter").value;
    const passwordVerify = document.getElementById("password-verify").value;
    if (passwordEnter == passwordVerify){
        await register(email, passwordVerify);
    }
    else{
        document.getElementById("register-error").innerText = "Passwords do not match! Try again."
    }

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
