document.getElementById("generate-button").addEventListener("click", async function() {
    document.getElementById("resume").srcdoc = await generate();
});

document.getElementById("download-html-button").addEventListener("click", async function() {
    html = await generate("html");
    downloadHtml("resume.html", html);
});

document.getElementById("download-pdf-button").addEventListener("click", async function() {
    pdf = await generate("pdf");
    downloadPdf("resume.pdf", pdf);
});

async function generate(type) {
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
                "type": type,
            })
        }
    );

    if (response.ok && type == "html") {
        return (await response.json())["resume"];
    } else if (response.ok && type == "pdf") {
        return await response.blob()
    }

}

function downloadHtml(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

function downloadPdf(filename, pdfData) {
    var blob = new Blob([pdfData], { type: 'application/pdf' });
    var url = URL.createObjectURL(blob);

    var element = document.createElement('a');
    element.setAttribute('href', url);
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
    URL.revokeObjectURL(url); // Clean up the URL object to free resources
}
