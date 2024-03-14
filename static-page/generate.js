document.getElementById("generate-button").addEventListener("click", async function() {
    document.getElementById("resume").srcdoc = await generate();
});

document.getElementById("download-html-button").addEventListener("click", async function() {
    // document.getElementById("resume").srcdoc = await generate();
});

async function generate() {
    const token = localStorage.getItem("token");
    const tags = ["tech"]; // TODO: Unhardcode
    const template = document.getElementById("template-selector").value;

    const response = await fetch(
        "http://127.0.0.1:5000/resume/generate",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "token": token,
                "tags": tags,
                "template": template,
                "type": "html",
            })
        }
    );

    if (response.ok) {
        return (await response.json())["resume"];
    }

}
