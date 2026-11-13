function arith() {
    var num1 = document.getElementById("num1");
    var num2 = document.getElementById("num2");
    var n1 = parseInt(num1.value);
    var n2 = parseInt(num2.value);
    document.getElementById("a").innerHTML = "" + (n1 + n2),
        document.getElementById("s").innerHTML = "" + (n1 - n2);
}
