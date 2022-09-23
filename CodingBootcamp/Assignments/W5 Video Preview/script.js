console.log("page loaded...");

function preview(element) {
    element.play()
    element.muted = true
    // element.playbackRate = 6
}

function stopPreview(element){
    element.pause()
    element.muted = false
    element.currentTime = 0
    // element.playbackRate = 4
}