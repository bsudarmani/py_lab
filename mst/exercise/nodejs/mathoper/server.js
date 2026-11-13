const express=require("express")
const app=express()
const os=require("os")
const path=require("path")
const fs=require("fs")
const port=3000
const mathlib=require('./math.js')
// let a=10
// let b=5
// console.log(mathlib.add(a,b))
// console.log(mathlib.sub(a,b))
// console.log(mathlib.mul(a,b))

// app.get('/',(req,res)=>
// {
//     res.send("hello")
// })

//os

console.log("Architecture:"+os.arch())
console.log("Total:"+os.totalmem())
console.log("Free:"+os.freemem())
console.log("info:"+os.platform())
console.log("homedir:"+os.homedir())
console.log("Type"+os.type())

// path
const filepath=path.join(__dirname,"files","sam.txt")

console.log(filepath)
console.log("basename:"+path.basename(filepath))
console.log("extname:"+path.extname(filepath))
console.log("dirname:"+path.dirname(filepath))


//file
const folder=path.join(__dirname,"files")
const file=path.join(folder,"sam.txt")

if(!fs.existsSync(folder))
{
    fs.mkdir(folder)
    console.log("folder created")
}
//create and write
fs.writeFileSync(file,"hello")
console.log("file created")

//read file
const data=fs.readFileSync(file,"utf8")
console.log("readed content:"+data)

//append
fs.appendFileSync(file,"append the data on the file")

console.log("file appended")

app.listen(port,()=>
{
    console.log(`server running at the port:${port}`)
})