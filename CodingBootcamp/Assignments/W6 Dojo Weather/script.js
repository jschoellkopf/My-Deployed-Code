var tempInCelciusOrFarenheit = 0;
var temperatures = [24,18,27,19,21,16,26,21]
var els = document.querySelectorAll("#temperature");


function loadingWeatherAlert() {
    alert('Loading weather report...')
}

function dismissCookie(element) {
    element.parentElement.remove()
}

function switchTemp() {
    if (tempInCelciusOrFarenheit %2 == 0) {
        for (let i = 0; i < els.length; i++) {
            els[i].innerText = CtoF(temperatures[i]) + "°";
            temperatures[i] = CtoF(temperatures[i])
        }
        console.log(temperatures)
    }
    else {
        for (let i = 0; i < els.length; i++) {
            els[i].innerText = FtoC(temperatures[i]) + "°";
            temperatures[i] = FtoC(temperatures[i])
        }
        console.log(temperatures)
    }
    tempInCelciusOrFarenheit += 1 
}

function FtoC(temp) {
    temp = ((temp-32)*5/9).toFixed(0)
    return temp
}

function CtoF(temp) {
    temp = ((temp*9/5)+32).toFixed(0)
    return temp
}

/* could have taken ° away from numbers and added it back in css
#temperature::after {
    content: "°";
} 
then give each temperature a unique id #temp1 through #temp8
using "this" for the button, to do an if element.value is == to °C 
function convert(element) {
    for (var i = 1; i < 9; i++) {
        var tempSpan = document.querySelector("#temp" + i);
        var tempVal = parseInt(tempSpan.innerText);
        if (element.value == "C°") {
            tempSpan.innerText = f2c(tempVal)
        } else {
            tempSpan.innerText = c2f(tempVal)
        }

    }
}

function c2f(temp) {
    return Math.round(9/5*temp+32)
}
function f2c(temp) {
    return Math.round(5/9*(temp-32))
}