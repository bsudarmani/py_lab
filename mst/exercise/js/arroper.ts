let nums:number[]=[]
function add()
{
    let num=document.getElementById("num") as HTMLInputElement
    let n1=parseInt(num.value)
    if(isNaN(n1))
    {
        alert("please enter the valid number")
        return;
    }
    nums.push(n1);
    (document.getElementById("list")!.textContent=nums.join(","))
    num.value="";
}
function sort()
{
    let sorted=[...nums].sort((a,b)=>a+b)
    let dsort=[...nums].sort((a,b)=>b-a);
    (document.getElementById("result")!.textContent=`sorted:${sorted} dsort:${dsort}`)
}