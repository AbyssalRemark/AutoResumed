var collapseButton = document.getElementsByClassName("collapse-button");
for (i = 0; i < collapseButton.length; i++) {
  collapseButton[i].addEventListener("click", function() {
    var toClose = document.getElementsByClassName("collapsible-element")
    var content = this.nextElementSibling;
    for (j = 0; j < toClose.length; j++){
        collapseButton[j].classList.remove("open")
        if (toClose[j] != content){
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
    addableId = addableId.slice(0,-4)
    var initAddable = (document.getElementsByClassName(addableId)[0]);
    var initRemoveButton = document.createElement("button")
    initRemoveButton.type="button"
    initRemoveButton.className="remove-button"
    initRemoveButton.innerText="Remove"
    initRemoveButton.addEventListener("click", function() {
        var buttonParent = this.parentElement;
        buttonParent.remove()
    })
    initAddable.appendChild(initRemoveButton)

    addButton[k].addEventListener("click", function() {
        var className = this.id.slice(0,-4)
        var toAddProto = prototypes.getElementsByClassName(className)[0];
        var toAdd = toAddProto.cloneNode(true);
        var newId = toAdd.id
        var splitId = newId.split("_")
        var siblings = this.parentElement.children
        var lastElement = siblings[siblings.length-1]
        var nextCount = parseInt(lastElement.id.split("_")[1]) + 1
        if (isNaN(nextCount)){
          nextCount = 0
        }
        splitId[1] = nextCount.toString()
        newId = splitId.join("_")
        toAdd.id = newId
        var addTo = this.parentElement;
        var removeButton = document.createElement("button")
        removeButton.type="button"
        removeButton.class='remove-button'
        removeButton.innerText="Remove"
        toAdd.appendChild(removeButton)
        addTo.appendChild(toAdd);

        removeButton.addEventListener("click", function() {
            var buttonParent = this.parentElement;
            buttonParent.remove()
        })
    })
}

function collectEntries(className){
  let resumeForm = document.getElementById("resume-form")
  let languageEntries = resumeForm.getElementsByClassName(className)
  let languages = []
  for (a = 0 ; a < languageEntries.length; a++) {
    let language = {}
    let fields = languageEntries[a].getElementsByClassName("input-field")
    for(b=0;b<fields.length;b++) {
      let fieldChildren = fields[b].children
      if (fieldChildren[1].tagName == "textarea"){
        language[fieldChildren[0].innerText.toLowerCase()]=fieldChildren[1].innerText
      }
      else{
        language[fieldChildren[0].innerText.toLowerCase()]=fieldChildren[1].value
      }
    }
    languages.push(language)
  }
  console.log(languages)
}
collectEntries("language-form-entry")