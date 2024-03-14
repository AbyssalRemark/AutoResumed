async function main() {
    let isAuth = await isAuthorized()

    const currentUrl = window.location.href;

    viewControl(isAuth)

    let redirectlist = ["https://autoresumed.com/resume.html", "https://autoresumed.com/generate.html"]
    if (redirectlist.includes(currentUrl)) {
        redirect(isAuth)
    }
}

async function isAuthorized() {
    let token = { 'token': localStorage.getItem('token') };
    let isAuthorized = await fetch("https://autoresumed.com/api/auth/is_authorized", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(token)
    });
    if (isAuthorized.ok) {
        let ret = (await isAuthorized.json())["authorized"];
        return ret
    }
    else {
        return false;
    }
}

function redirect(bool) {
    if (!bool()) {
        window.location.replace("https://autoresumed.com/index.html")
    }
}

function viewControl(bool) {
    var loggedIn = document.getElementById("logged-in");
    var loggedOut = document.getElementById("logged-out");
    if (bool) {
        loggedIn.style.display = "block";
        loggedOut.style.display = "none";
    }
    else {
        loggedIn.style.display = "none";
        loggedOut.style.display = "block";
    }
}

main();
