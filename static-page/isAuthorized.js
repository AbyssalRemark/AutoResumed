export async function isAuthorized() {
    let token = { 'token': localStorage.getItem('token') };
    let isAuthorized = await fetch("http://0.0.0.0/auth/is_authorized", {
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
