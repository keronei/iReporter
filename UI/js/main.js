var field = document.getElementById("user_location_field");


//Geolocation services functions
function getUserLocation(){
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(appendLocation,handleError);
    }else{
        field.innerHTML = "Unfortunately your browser doesn't support Geolocation";
        
    }
}

function appendLocation(position){
    field.innerHTML = "Lat: " + position.coords.latitude + "Long: " + position.coords.latitude;
}

function handleError(error){
    switch(error.code){
        case error.PERMISSION_DENIED:
            field.innerHTML = "Please allow your browser to access location";
            break;
        case error.POSITION_UNAVAILABLE:
            field.innerHTML = "Location Info not available";
            break;
        case error.TIMEOUT:
            field.innerHTML = "Your request timed out, please retry";
            break;
        case error.UNKNOWN_ERROR:
            field.innerHTML = "Sorry, unknown error occured !";
    }
    
}

//Menu transitions starts here
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "rgb(219,193,153)";
}

   
function menuOrganizer(toActivate){


    var nextDiv = document.getElementById(toActivate);

    var divLanding = document.getElementById("landing_screen");
    var divNewEntry = document.getElementById("create_entry");
    var divUpdateEntry = document.getElementById("update_entry");
    var divViewEntry = document.getElementById("view_entries");
    var divProfileEntry = document.getElementById("user_profile");
    
   var divs = [divNewEntry,divUpdateEntry,divViewEntry,divProfileEntry,divLanding];
    
    var divCount;
    for ( divCount = 0;divCount < divs.length;divCount++ ){
       
        if (divs[divCount].style.display == "block"){
            divs[divCount].style.display = "none";
            
            
        }else{
         nextDiv.style.display = "block";
        }
    } 


}
function confirmDeletion(){
    window.alert('Are you sure you want to completely remove this entry?');
}

function swapLogin(activate){
       var divLogin = document.getElementById("login");
       var divsignup = document.getElementById("signup");
       
       if (activate == 'signin'){
         divLogin.style.display = "block";
         divsignup.style.display = "none";
       }else{
         divLogin.style.display = "none";
         divsignup.style.display = "block";
       }
       
       
}
function goto_home(){
   window.open("home.html","_self");
}