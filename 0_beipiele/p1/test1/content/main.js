function change_view(idContainer){
    var element_o = document.getElementById(idContainer);
    
    
    if (element_o.style.display != "none"){
        
        element_o.style.display = "none";
    }
        else{
            
            element_o.style.display = "block";
        }
    
 } 
