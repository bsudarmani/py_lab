const express=require('express')
const cors=require('cors')
const mongoose=require('mongoose')

const app=express()
app.use(cors())
app.use(express.json())
mongoose.connect('mongodb://127.0.0.1:27017/login')
.then(()=>console.log("db is connected"))
.catch(()=>console.log("not connected"))
// mongodb://127.0.0.1:27017/loginDB

const User=mongoose.model('users',{
    username:String,
    password:String
})



app.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;

        console.log("Entered Username:", username);
        console.log("Entered Password:", password);

        const user = await User.findOne({
            username: username
        });

        console.log("MongoDB User:", user);

        if (user && user.password === password) {

            console.log("Sending success response");

            return res.status(200).send("Login Successfully");
        }
        else {

            console.log("Sending invalid response");

            return res.status(401).send("Invalid Username or Password");
        }

    }
    catch (err) {
        console.log("Error:", err);
        return res.status(500).send("Server Error");
    }
});



app.post('/regiser',async(req,res)=>
{
    const user=new User(req.body)
    await user.save()
    res.send("user registered successfully")
})

app.listen(3000,()=>
{
    console.log("port running at the 3000")
})