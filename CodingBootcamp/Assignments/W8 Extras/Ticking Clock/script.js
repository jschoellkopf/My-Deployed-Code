function getSecondsSinceStartOfDay() {
    return new Date().getSeconds() + 
      new Date().getMinutes() * 60 + 
      new Date().getHours() * 3600;
}

// var hourAngle = 360/(60*60*12) // degree change per second
// var minuteAngle = 360/(60*60) // = 0.1
// var secondAngle = 360/60 // = 6

var hour_starting_angle = (getSecondsSinceStartOfDay()*(1/120))%360+180; //same as 360/43200 = 0.083333
console.log(hour_starting_angle);
var min_starting_angle = (getSecondsSinceStartOfDay()*0.1)%360+180;
console.log(min_starting_angle);
var sec_starting_angle = (getSecondsSinceStartOfDay()*6)%360+180;
console.log(sec_starting_angle);

setInterval( function() {
    var time = getSecondsSinceStartOfDay();
    console.log(time);
    secHand = document.getElementById("seconds")
    secHand.style.webkitTransform = 'rotate('+sec_starting_angle+'deg)';
    sec_starting_angle += 6 // 360 / 60
    minHand = document.getElementById("minutes")
    minHand.style.webkitTransform = 'rotate('+min_starting_angle+'deg)';
    min_starting_angle += 0.1 // 360/(60*60)
    hourHand = document.getElementById("hour")
    hourHand.style.webkitTransform = 'rotate('+hour_starting_angle+'deg)';
    hour_starting_angle += (360/43200) // 360/(60*60*12)
}, 1000);
