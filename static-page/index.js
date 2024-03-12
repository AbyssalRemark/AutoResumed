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

async function login(email, password) {
    const response = await fetch(
        "http://127.0.0.1:5000/auth/login",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "email": email, "password": password })
        }
    );

    const token = response.json()["token"];
    localStorage.setItem("token", token);
}

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

    localStorage.removeItem("token");
}

async function _delete(token) {
    await fetch(
        "http://127.0.0.1:5000/auth/delete",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "token": token })
        }
    );

    localStorage.removeItem("token");
}
