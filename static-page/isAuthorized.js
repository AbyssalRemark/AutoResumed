export async function isAuthorized() {
    let token = { 'token': localStorage.getItem('token') };
    let isAuthorized = await fetch("https://autoresumed.com/auth/is_authorized", {
        method: "POST",
        body: JSON.stringify(token)
    });
    if (isAuthorized.ok) {
        let ret = (await isAuthorized.json())["authorized"];
        return ret
    }
    else {
        return False;
    }
}

export function redirect(bool){
    if(!bool()){
        window.location.replace("https://autoresumed.com/index.html")
    }
}

export function viewControl(bool){
    var loggedIn = document.getElementById("logged-in");
    var loggedOut = document.getElementById("logged-out");
    if(bool){
        loggedIn.style.display="block";
        loggedOut.style.display="none";
    }
    else{
        loggedIn.style.display="none";
        loggedOut.style.display="block";
    }
}

let isAuth=isAuthorized()

viewControl(isAuth)
redirect(isAuth)