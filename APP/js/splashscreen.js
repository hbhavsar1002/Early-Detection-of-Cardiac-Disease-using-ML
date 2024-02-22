(function(){
    
    var preload = document.getElementsByClassName("center");
    var loading = 0;
    var id = setInterval(frame,31);
    
    function frame(){
        
        if(loading == 100){
            
            clearInterval(id);
            window.open("newlogin.html","_self");
        }
        else {
            
            loading= loading + 1;
            if(loading == 90){
                
                preload.style.animation = "fadeout 3s ease";
            }
        }
    }
    
}



)();