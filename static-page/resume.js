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
console.log(addButton)
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
        var existingCount = this.parentElement.children.length - 2
        splitId[1] = existingCount.toString()
        newId = splitId.join("_")
        toAdd.id = newId
        var innerElements = toAdd.children
        for(a = 0; a<innerElements; a++){
          newIdInner = innerElements[a].id
          var splitIdInner = newIdInner.split("_")
          splitIdInner[1] = existingCount.toString()
          newIdInner = splitId.join("_")
          innerElements[a].id = newIdInner
          
        }
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

