async function logout(token) {
    await fetch(
        "http://127.0.0.1:5000/auth/logout",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "token": token })
        }
    );

    if (response.ok) {
        localStorage.removeItem("token");
    }
}
