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
