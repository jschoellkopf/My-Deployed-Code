var number = 0
var operator =""
var number2 = 0
var calc = 0


setTimeout(alert,3000, "THIS CALCULATOR CAN ONLY CALCULATE 2 DIFFERENT NUMBERS, HAVE FUN!")

function press(nbr){
    if (calc == 0){
        if ($("#display").html() == "0" && nbr == 0 ){ //I don't want to be able to add "0"s in a line
        }
        else if ($("#display").html() == "0"){
            if (nbr == ".") {
                $("#display").append(nbr); // if "." pressed, the "0" stays
            }
            else { 
                $("#display").html(nbr); // otherwise it disapears to show the number clicked
            }
        }
        else {
            $("#display").append(nbr); // otherwise jsut add the number on the display
        }
    }
    else {
        $("#display").html(nbr); // to be able to continue calculation after having used calculate()
        calc = 0
    }
}

function setOP(oper){
    number = $("#display").html();
    number = Number(number) //setting number when pressing operator, tunring it from string to number
    // console.log(number);
    $("#display").html(0);
    operator = oper
    // console.log(operator);
}

function clr() {
    $("#display").html(0);
    number = 0
}

function calculate(){
    number2 = $("#display").html(); 
    number2 = Number(number2)
    // not sure how to use the operator as a variable to be able to calculate
    // number operator number2 = ...
    if (operator == "+") {
        $("#display").html(number+number2)
    }
    else if (operator == "-") {
        $("#display").html(number-number2)
    }
    else if (operator == "*") {
        $("#display").html(number*number2)
    }
    else if (operator == "/") {
        $("#display").html(number/number2)
    }

    calc = 1
    number = 0
    number2 = 0
}