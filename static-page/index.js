const resumeHelp = new Audio("cowboy/resume-help.mp3")

document.getElementById("cowboy-ready").addEventListener("click", function() {
    resumeHelp.play();
})
