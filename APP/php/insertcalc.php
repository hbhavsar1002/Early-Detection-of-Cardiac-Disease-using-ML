<?php
include "db.php";



    $age =$_POST['age']; 
    $sex =$_POST['sex']; 
    $cp =$_POST['cp']; 
    $trestbps =$_POST['trestbps']; 
    $chol =$_POST['chol']; 
    $fbs =$_POST['fbs']; 
    $restecg =$_POST['restecg']; 
    $thalach =$_POST['thalach']; 
    $exang =$_POST['exang']; 
    $oldpeakst =$_POST['oldpeakst']; 
    $slope =$_POST['slope']; 
    $ca =$_POST['ca']; 
    $thal =$_POST['thal']; 
    
    $strSql= "INSERT INTO `infogather`(`id`, `age`, `sex`, `cp`, `trestbps`, `cholestrol`, `fbs`, `testecgval`, `maxheartrate`, `exangina`, `oldpeakst`, `slope`, `ca`, `thal`) VALUES (null, '$age','$sex','$cp','$trestbps','$chol', '$fbs','$restecg','$thalach','$exang','$oldpeakst','$slope','$ca','$thal')";
 
   $q = mysqli_query($con,$strSql);

    if($q){
         echo "success";
    }else{
        echo "error".$q ;
    }
  
 
 
    

?>