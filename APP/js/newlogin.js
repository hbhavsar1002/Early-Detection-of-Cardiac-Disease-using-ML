 $(document).ready(function(){
                
               
                
                $("#username").keyup(function(){
                    
                        
                    var regex = /^[a-zA-Z0-9._@]{2,15}$/;
                    if(regex.test($("#username").val())){
                   
                    $("#username").removeClass("has-error");
                        $("#username").addClass("has-success");
                        
                    }else{
                       
                        $("#username").addClass("has-error");
                    } 
                    
            
                    
                });
                
                
                 $("#password").keyup(function(){
                    
                        
                    var regex = /^[a-zA-Z0-9.@]{4,15}$/;
                    if(regex.test($("#pass").val())){
                   
                    $("#pass").removeClass("has-error");
                        $("#pass").addClass("has-success");
                        
                    }else{
                       
                        $("#pass").addClass("has-error");
                    } 
                    
                });
                
                
                
                $("#login").click(function(event){
                    
                    event.preventDefault();
                    
                   
                    var username = $("#username").val();
                  
                    var password = $("#password").val();
                       
                    
                    var datastring1 =  "&username=" + username + "&password=" + password;
                    
                    console.log(datastring1);
                    
                    
                
                    
                 if ( $.trim(username).length > 0  &  $.trim(password).length > 0){
                        
                        $.ajax({
                            type:"POST",
                            url: "newlogin.php",
                            data: datastring1,
                            cache:false,
                            beforeSend: function(){ $("#login").val('Connecting...');},
                          success: function(data)
                            {
                              
                                alert(data);
                                if(data=="success")
                            {
                                alert("Login successful");

                                 window.location.href="home.html";
                            }
                            else if(data=="error")
                            {
                                alert("error");
                            }
                            }
                        });
               }
                    return false;
                    
                    });
                    });
                    