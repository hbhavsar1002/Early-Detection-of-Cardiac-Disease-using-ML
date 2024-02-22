
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("myBtn").style.display = "block";
  } else {
    document.getElementById("myBtn").style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

  <!-- Menu Toggle Script -->

      $(document).ready(function(){


                $("#age").keyup(function(){

                    var regex = /^[0-9]{1,2}$/;
                    if($("#age").val() > 100 || $("#age").val() < 0 ){

                    $("#error").show();
                    $("#error").addClass("has-error");


                    }else{


                         $("#error").removeClass("has-error");
                         $("#error").hide();
                    }
                })

              $("#ca").keyup(function(){


                    if($("#ca").val() > 3 || $("#ca").val() < 0){

                    $("#error_a").show();
                    $("#error_a").addClass("has-error");


                    }else{


                         $("#error_a").removeClass("has-error");
                         $("#error_a").hide();
                    }
                })

          $("#subbtn").click(function(){

                    var age = $("#age").val();
                    var sex = $("#sex").val();
                    var cp = $("#cp").val();
                    var trestbps = $("#trestbps").val();
                    var chol = $("#chol").val();
                    var fbs =$("#fbs").val();
                    var restecg = $("#restecg").val();
                    var thalach = $("#thalach").val();
                    var exang = $("#exang").val();
                    var oldpeakst = $("#oldpeakst").val();
                    var slope = $("#slope").val();
                    var ca = $("#ca").val();
                    var thal =$("#thal").val();


               var dataformm = "age="+age+"&sex="+sex+"&cp="+cp+"&trestbps="+trestbps+"&chol="+chol+"&fbs="+fbs+"&restecg="+restecg+"&thalach="+thalach+"&exang="+exang+"&oldpeakst="+oldpeakst+"&slope="+slope+"&ca="+ca+"&thal="+thal;


              console.log(dataformm);

              $.ajax({

                  url: "insertcalc.php?",
                  type : "POST",
                  data : dataformm,
                  beforeSend: function(){ $("#subbtn").val('Connecting...');},
                  cache:false,
                  success: function(data)
                            {
                            $("#hello").html(data);
                            if( data == "success" )
                            {

                                alert("Registration successful");

                                 window.location.href="home.html";
                            }
                            else if(data=="error")
                            {
                                alert("error");
                            }


                            }


              })

          });


      });
    $("#menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("toggled");
    });
