let welcomeBtn = document.getElementById("welcomeBtn")
let welcomeBtnLi = document.getElementById("welcomeBtn1")
let background = document.querySelector("body")



function select(e){
    click(e)
    transition()
    
}
function select2(e){
    click2(e)
    transition2()
    
}
function hover(e){
    setTimeout(() => {
        welcomeBtn.innerText = `Login!`
        welcomeBtn.setAttribute("class" , "loginswitch-btn")
    }, 100);
}
function hover2(e){
    setTimeout(() => {
        welcomeBtnLi.innerText = `Enter!`
        
        // welcomeBtnLi.removeAttribute("class" , "loginswitch-btn")
    }, 100);
}
function returnWelcome(e){

    setTimeout(() => {
        welcomeBtnLi.innerText = `Welcome!`
        welcomeBtnLi.setAttribute("class" , "welcome-btn")
    }, 100);

}
function returnWelcome2(e){

    setTimeout(() => {
        welcomeBtn.innerText = `Welcome!`
        welcomeBtn.setAttribute("class" , "welcome-btn")
    }, 100);

}
if(welcomeBtnLi){
    welcomeBtnLi.addEventListener("click" , select2 )
    welcomeBtnLi.addEventListener("mouseover" , hover2)
    welcomeBtnLi.addEventListener("mouseleave" , returnWelcome)
}else{
    welcomeBtn.addEventListener("click" , select )
    welcomeBtn.addEventListener("mouseover" , hover)
    welcomeBtn.addEventListener("mouseleave" , returnWelcome2)
}






function click(e){
  
        e.preventDefault()
        background.setAttribute("class", "entryBackground")
        welcomeBtn.setAttribute("class", "clickedWelcome")
   
 
}
function click2(e){
  
        e.preventDefault()
        background.setAttribute("class", "entryBackground")
        welcomeBtnLi.setAttribute("class", "clickedWelcome")
   
 
}




function transition(){
        setTimeout(function(){
            welcomeBtn.removeEventListener("click",select)
            welcomeBtn.click()
            console.log("clicked")
            
        },1300)
    
    
}
function transition2(){
        setTimeout(function(){
            welcomeBtnLi.removeEventListener("click",select2)
            welcomeBtnLi.click()
            console.log("clicked")
            
        },1300)
    
    
}