var count1 = 9
var count2 = 12
var count3 = 9

function add1Like() {
    var likeElement = document.querySelector(".likeNbr")
    count1 ++
    likeElement.innerText = count1 + " like(s)"
}
function add1Like2() {
    var likeElement = document.querySelector(".likeNbr2")
    count2 ++
    likeElement.innerText = count2 + " like(s)"
}
function add1Like3() {
    var likeElement = document.querySelector(".likeNbr3")
    count3 ++
    likeElement.innerText = count3 + " like(s)"
}

function scale(element, value, bcolor) {
    element.style.transform = "scale(" + value + ")";
    element.style.backgroundColor = bcolor
}

function change_background(element) {
}