
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
        addEntry(className)

/*      Yay put this outside so its reusable by another funcation!

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
        */
    })
}

function addEntry(className) {
    var elementId = className.concat("-add");
    var thisElement = document.getElementById(elementId);
    var parentElement = thisElement.parentElement;
    var toAddProto = prototypes.getElementsByClassName(className)[0];
    var toAdd = toAddProto.cloneNode(true);
    var newId = toAdd.id;
    var splitId = newId.split("_");
    var siblings = parentElement.children;
    var lastElement = siblings[siblings.length - 1];
    var nextCount = parseInt(lastElement.id.split("_")[1]) + 1;
    if (isNaN(nextCount)) {
        nextCount = 0;
    }
    splitId[1] = nextCount.toString();
    newId = splitId.join("_");
    toAdd.id = newId;
    var addTo = parentElement;
    var removeButton = document.createElement("button");
    removeButton.type = "button";
    removeButton.class = 'remove-button';
    removeButton.innerText = "Remove";
    toAdd.appendChild(removeButton);
    addTo.appendChild(toAdd);

    removeButton.addEventListener("click", function() {
        var buttonParent = this.parentElement;
        buttonParent.remove();
    })
}

function collectEntries(className) {
    let resumeForm = document.getElementById("resume-form");
    let elements = resumeForm.getElementsByClassName(className);
    let entries = [];
    for (a = 0; a < elements.length; a++) {
        let entry = {};
        let fields = elements[a].getElementsByClassName("input-field");
        for (b = 0; b < fields.length; b++) {
            let fieldChildren = fields[b].children;
            if (fieldChildren[1].tagName == "textarea") {
                entry[camelCase(fieldChildren[0].innerText)] = fieldChildren[1].innerText;
            }
            else {
                entry[camelCase(fieldChildren[0].innerText.toLowerCase())] = fieldChildren[1].value;
            }
        }
        entries.push(entry);
    }
    return entries;
}

function loadEntry(entry,className) {
    let resumeForm = document.getElementById("resume-form");
    let form = resumeForm.getElementsByClassName(className);
    if(className!=="name-form-entry"&&className!=="location-form-entry"){
        while (entry.length > form.length){
            addEntry(className);
            form = resumeForm.getElementsByClassName(className);
        }

        for(i=0;i<entry.length;i++){
            let elements = form[i].children
            for(j=0;j<elements.length-1;j++){
                let fields = elements[j].children
                let key = camelCase(fields[0].innerText)
                if(className=="label-form-entry"&&key=="position"){
                    key="label"
                }
                if(fields[1].type=="textarea"){
                    fields[1].innerText=entry[i][key]
                }
                if(fields[1].tagName=="DIV"){
                    let thisDiv = fields[1]
                    let listElement = thisDiv.children[0]
                    let listLoad = entry[i][key]
                    for(k=0;k<listLoad.length;k++){
                        let listItem = document.createElement("li")
                        listItem.textContent = listLoad[k]
                        listElement.appendChild(listItem)
                    }
                }
                else{
                    fields[1].value=entry[i][key]
                }
            }
        }
    }
    else{
        elements = form[0].children
        for(i=0;i<elements.length;i++){
            let field = elements[i]
            let label = field.children[0]
            let key = camelCase(label.innerText)
            let content = entry[key]
            field.children[1].value=content
        }
    }
}

function addListItem(addItemButton) {
    const parentDiv = addItemButton.parentNode
    const inputField = parentDiv.children[1]
    const list = parentDiv.children[0]
    const newItem = inputField.value
    if(newItem.lenght>3){
        newItem.value = "";
        const listItem = document.createElement("li");
        listItem.textContent = newItem;
        const removeBtn = document.createElement("button");
        removeBtn.textContent = "[X]";
        removeBtn.classList.add("list-remove-button");
        removeBtn.addEventListener("click", function() {
            listItem.remove();
        });
        listItem.appendChild(removeBtn);
        list.appendChild(listItem);
    }
}


function collectResume(){
    let resume = {};
    resume["basics"]=collectEntries("name-form-entry")[0];
    resume["basics"]["location"]=collectEntries("location-form-entry")[0];
    resume["basics"]["label"]=collectEntries("label-form-entry");
    resume["basics"]["summary"]=collectEntries("summary-form-entry");
    resume["basics"]["profile"]=collectEntries("profile-form-entry");
    resume["work"]=collectEntries("work-form-entry");
    resume["volunteer"]=collectEntries("volunteer-form-entry");
    resume["education"]=collectEntries("education-form-entry");
    resume["awards"]=collectEntries("award-form-entry");
    resume["certificates"]=collectEntries("certificate-form-entry");
    resume["publications"]=collectEntries("publication-form-entry");
    resume["skills"]=collectEntries("skill-form-entry");
    resume["references"]=collectEntries("reference-form-entry");
    resume["projects"]=collectEntries("project-form-entry");
    resume["languages"]=collectEntries("language-form-entry");
    resume["interests"]=collectEntries("interest-form-entry");
    return resume
}

function camelCase(str) {
    let ans = str.toLowerCase();
     return ans.split(" ").reduce((s, c) => s
        + (c.charAt(0).toUpperCase() + c.slice(1)));
 
}

function loadResume(resume){
    alert(resume)
}

async function testLoad(){
    var testResume = await fetch("https://autoresumed.com/testResume.json") .then(function(response) {
        return response.json();
    })
    loadEntry(testResume["work"],"work-form-entry");
    loadEntry(testResume["volunteer"],"volunteer-form-entry");
    loadEntry(testResume["education"],"education-form-entry");
    loadEntry(testResume["awards"],"award-form-entry");
    loadEntry(testResume["certificates"],"certificate-form-entry");
    loadEntry(testResume["publications"],"publication-form-entry");
    loadEntry(testResume["skills"],"skill-form-entry");
    loadEntry(testResume["references"],"reference-form-entry");
    loadEntry(testResume["projects"],"project-form-entry");
    loadEntry(testResume["languages"],"language-form-entry");
    loadEntry(testResume["interests"],"interest-form-entry");
    loadEntry(testResume["basics"],"name-form-entry");
    loadEntry(testResume["basics"]["location"],"location-form-entry");
    loadEntry(testResume["basics"]["label"],"label-form-entry");
    loadEntry(testResume["basics"]["summary"],"summary-form-entry");
    loadEntry(testResume["basics"]["profiles"],"profile-form-entry");
   

}

testLoad()