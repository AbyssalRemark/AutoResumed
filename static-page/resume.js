var mainDiv = document.getElementsByTagName("main")[0]
var collapseButton = mainDiv.getElementsByClassName("collapse-button");
for (i = 0; i < collapseButton.length; i++) {
    collapseButton[i].addEventListener("click", function() {
        var toClose = mainDiv.getElementsByClassName("collapsible-element")
        var content = this.nextElementSibling;
        for (j = 0; j < collapseButton.length; j++) {
            collapseButton[j].classList.remove("open")
            if (toClose[j] != content) {
                toClose[j].style.display = "none";
            }
        }
        this.classList.add("open");
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}

var addButton = document.getElementsByClassName("add-button");
var prototypes = document.getElementById("element-prototypes")
for (k = 0; k < addButton.length; k++) {
    addableId = addButton[k].id
    addableId = addableId.slice(0, -4)
    var initAddable = (document.getElementsByClassName(addableId)[0]);
    var initRemoveButton = document.createElement("button")
    initRemoveButton.type = "button"
    initRemoveButton.className = "remove-button"
    initRemoveButton.innerText = "Remove"
    initRemoveButton.addEventListener("click", function() {
        var buttonParent = this.parentElement;
        buttonParent.remove()
    })
    initAddable.appendChild(initRemoveButton)

    addButton[k].addEventListener("click", function() {
        var className = this.id.slice(0, -4)
        var toAddProto = prototypes.getElementsByClassName(className)[0];
        var toAdd = toAddProto.cloneNode(true);
        var newId = toAdd.id
        var splitId = newId.split("_")
        var siblings = this.parentElement.children
        var lastElement = siblings[siblings.length - 1]
        var nextCount = parseInt(lastElement.id.split("_")[1]) + 1
        if (isNaN(nextCount)) {
            nextCount = 0
        }
        splitId[1] = nextCount.toString()
        newId = splitId.join("_")
        toAdd.id = newId
        var addTo = this.parentElement;
        var removeButton = document.createElement("button")
        removeButton.type = "button"
        removeButton.class = 'remove-button'
        removeButton.innerText = "Remove"
        toAdd.appendChild(removeButton)
        addTo.appendChild(toAdd);

        removeButton.addEventListener("click", function() {
            var buttonParent = this.parentElement;
            buttonParent.remove()
        })
    })
}

function collectEntries(className) {
    let resumeForm = document.getElementById("resume-form");
    // TODO: This isn't named right
    let elements = resumeForm.getElementsByClassName(className);
    let entries = [];
    for (a = 0; a < elements.length; a++) {
        let entry = {};
        let fields = elements[a].getElementsByClassName("input-field");
        for (b = 0; b < fields.length; b++) {
            let fieldChildren = fields[b].children;
            if (fieldChildren[1].tagName == "textarea") {
                entry[fieldChildren[0].innerText.toLowerCase()] = fieldChildren[1].innerText;
            }
            else {
                entry[fieldChildren[0].innerText.toLowerCase()] = fieldChildren[1].value;
            }
        }
        entries.push(entry);
    }
    return entries;
}



function collectResume(){
    let resume = {}
    resume["basics"]=collectEntries("name-form-entry")[0]
    resume["basics"]["location"]=collectEntries("location-form-entry")[0]
    resume["basics"]["label"]=collectEntries("label-form-entry")
    resume["basics"]["summary"]=collectEntries("summary-form-entry")
    resume["basics"]["profile"]=collectEntries("profile-form-entry")
    resume["work"]=collectEntries("work-form-entry")
    resume["volunteer"]=collectEntries("volunteer-form-entry")
    resume["education"]=collectEntries("education-form-entry")
    resume["awards"]=collectEntries("award-form-entry")
    resume["certificates"]=collectEntries("certificate-form-entry")
    resume["publications"]=collectEntries("publication-form-entry")
    resume["skills"]=collectEntries("skill-form-entry")
    resume["references"]=collectEntries("reference-form-entry")
    resume["projects"]=collectEntries("project-form-entry")
    resume["languages"]=collectEntries("language-form-entry")
    resume["interests"]=collectEntries("interest-form-entry")
    return resume
}

