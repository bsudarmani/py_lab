function arith():void
{
    let num1=document.getElementById("num1") as HTMLInputElement
    let num2=document.getElementById("num2") as HTMLInputElement
    let n1=parseInt(num1.value);
    let n2=parseInt(num2.value);
    (document.getElementById("a") as HTMLInputElement).innerHTML=""+(n1+n2),
    (document.getElementById("s") as HTMLInputElement).innerHTML=""+(n1-n2)
}