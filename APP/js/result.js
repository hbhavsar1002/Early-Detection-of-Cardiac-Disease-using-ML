$(document).ready(function(){
        $("#btn").click(function(){
         
         var value =  $("#data").text();
      if(value == "1"){
      		$("#has-error").show();
            $("#has-error").html("You have heart disease");
      	
      }else{
      			      		$("#has-success").show();
            $("#has-success").html("You do not have heart disease");
      	}
        });
    
        
    });