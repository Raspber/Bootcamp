// And the following code snippets:

// var displayDiv = document.querySelector("#display");
// displayDiv.innerText = "Some new value";
console.log("hello world")


var displayDiv = document.querySelector("#display");
var operator = "";
var num1 = "";
var num2 = "";


function press(num) {
    if (displayDiv.innerText == 0 || operator != "") {
        displayDiv.innerText = num;
    } else {
        displayDiv.innerText += num;
    }
}

function clr() {
    displayDiv.innerText = 0;
}

function setOP(op) {
    num1 = displayDiv.innerText;
    operator = op;{
    }
}
// = BUTTON
function calculate() {
    num2 = displayDiv.innerText;
    if (operator == "+") {
        displayDiv.innerText = parseInt(num1) + parseInt(num2);
    }
    else if (operator == "*") {
        displayDiv.innerText = parseInt(num1) * parseInt(num2);
    }
    else if (operator == "-") {
        displayDiv.innerText = parseInt(num1) - parseInt(num2);
    }
    else if (operator == "/") {
        displayDiv.innerText = parseInt(num1) / parseInt(num2);
    }
}