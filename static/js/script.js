console.log("hello world")
const buybtn=document.querySelector("#buy")
buybtn.addEventListener("onclick",()=>{
    location.href("{%url 'home'%}")

})