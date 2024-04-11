import User from "./user.js"

let regbutton=document.getElementById("regbtn")
let authbtn=document.getElementById("authbutton")

regbutton.addEventListener("click",()=>{
    registration()
    // window.open("index.html")
    
})
authbtn.addEventListener("click",()=>{
    auth()
    // window.open("index.html")
    
})

function registration(){
    let usernameField=document.getElementById("regname")
    let username=usernameField.value
    let emailField=document.getElementById("regemail")
    let email=emailField.value
    let passField=document.getElementById("regpass")
    let password=passField.value
    if(localStorage.getItem(email)) {
        alert("Такой email уже существует")

        
    }else{
        localStorage.setItem(email,password)
        window.location.href="index.html"
        }
}

function auth(){
    let emailField=document.getElementById("logemail")
    let email=emailField.value
    let passField=document.getElementById("logpass")
    let password=passField.value

    if(localStorage.getItem(email)===password) {
        window.location.href="index.html"
        
    }else{
       alert("Неверный логин или пароль")
        }
}



