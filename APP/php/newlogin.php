<?php

 include "db.php";

 if(isset($_POST['sub1']))
 {
     
  $username=$_POST['username'];
  $pass=$_POST['password'];
  $salt='3x%%$bf83#dls2qgdf';
  $passwo=md5($salt.$pass);

  
    
  $login = mysqli_num_rows(mysqli_query($con, "SELECT * FROM `registration` WHERE `username`='$username' AND `password`='$passwo'"));
     
  
    if($login == 1)
        echo "success";
    else
        echo "error";
     
     
    
 }

   
 ?>