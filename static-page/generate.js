document.getElementById("generate-button").addEventListener("click", async function() {
    document.getElementById("resume").srcdoc = await generate("html");
});

document.getElementById("download-html-button").addEventListener("click", async function() {
    html = await generate("html");
    downloadHtml("resume.html", html);
});

document.getElementById("download-pdf-button").addEventListener("click", async function() {
    pdf = await generate("pdf");
    downloadPdf("resume.pdf", pdf);
});

setupTagSelector();

async function setupTagSelector() {
    const tags = await getTags();
    console.log(tags);
    const tagSelector = document.getElementById("tag-selector");
    for (let tag = 0; tag < tags.length; tag++) {
        const div = document.createElement("div");

        const checkbox = document.createElement("input");
        checkbox.id = "checkbox-" + tag;
        checkbox.type = "checkbox"
        const label = document.createElement("label");
        label.htmlFor = "checkbox-" + tag;
        label.textContent = tags[tag];

        div.appendChild(checkbox);
        div.appendChild(label);

        tagSelector.appendChild(div);
    }
}

async function generate(type) {
    const token = localStorage.getItem("token");
    const tags = ["tech"]; // TODO: Unhardcode
    const template = document.getElementById("template-selector").value;

    const response = await fetch(
        "https://autoresumed.com/api/resume/generate",
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

async function getTags() {
    const token = localStorage.getItem("token");

    const response = await fetch(
        "https://autoresumed.com/api/resume/tags",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "token": token,
            })
        }
    );

    if (response.ok) {
        return (await response.json())["tags"];
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
