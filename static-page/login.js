document.getElementById("login-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    await login(email, password);
});

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
    )

    if (response.ok) {
        const token = (await response.json())["token"];
        localStorage.setItem("token", token);
    }
}

// async function _delete(token) {
//     await fetch(
//         "http://127.0.0.1:5000/auth/delete",
//         {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify({ "token": token })
//         }
//     );
//
//     localStorage.removeItem("token");
// }
