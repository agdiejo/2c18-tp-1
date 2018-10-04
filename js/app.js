const express= require("express")
const app = express()

//const PORT = 8000
const PORT = process.argv[2];

app.get("/veloz",(req,res)=>{
    res.send("hola desde veloz js desde puerto " + PORT)
})

app.get("/timeout",(req,res)=>{
    setTimeout(()=>{
        res.send("hola desde timeout js")
    },10000)
})


app.listen(PORT,"0.0.0.0",()=>{
    console.log("ESto escuchando en el puerto", PORT)
})