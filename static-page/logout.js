async function logout(token) {
    await fetch(
        "https://autoresumed.com/api/auth/logout",
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
