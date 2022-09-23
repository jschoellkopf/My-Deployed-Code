var requests = 2
var connections = 418

function changeName() {
    document.querySelector("#profileName").innerHTML = "Tori Bakuza"
}

function acceptRequestAndDelete(element) {
    element.parentElement.parentElement.remove()
    requests --
    document.querySelector(".nbrOfRequests").innerHTML = requests
    connections ++
    document.querySelector(".nbrOfConnections").innerHTML = connections
}

function refuseRequestAndDelete(element) {
    /*    document.querySelector("#todd").remove() */
        element.parentElement.parentElement.remove()
        requests --
    document.querySelector(".nbrOfRequests").innerHTML = requests
    }
