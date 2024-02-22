<?php 
    include "db.php";
   //if(isset($_POST['submit'])){
        
        $fname=$_POST['firstname'];
     
      
        
        $lname=$_POST['lastname'];
      
      
        
     
        
         $uname=$_POST['username'];
        
         $eml=$_POST['email'];
         $sex=$_POST['gender'];
         $passw =$_POST['password'];
    
         $salt='3x%%$bf83#dls2qgdf';
         $passwo=md5($salt.$passw);

       /* $strSQL = "INSERT INTO registration (`firstname`,`lastname`,`username`, `email`, `gender`, `password`) VALUES ('$fname', '$lname', '$uname', '$eml', '$sex', '$passw')";*/

        $sql = "INSERT INTO `registration`(`id`, `firstname`, `lastname`, `username`, `emailid`, `gender`, `passsword`) VALUES (null, '$fname', '$lname', '$uname', '$eml', '$sex', '$passwo')";

         $w=mysqli_query($con,$sql);
        
        if($w){
            
            echo "success";
            exit;
        }else{
            
            echo "error";
            
        }
  // }



?>