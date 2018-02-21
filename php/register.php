<!DOCTYPE html>
<html>
<body>
<h1> Welcome to the signup page </h1>

<form action="" method="POST">
  <input type="text" name="username">
  <input type="password" name="password">
  <input type="submit" name="submitButton">
</form>

<?php

  if(isset($_POST['submitButton'])){ //check if form was submitted
    $name = $_POST['username']; //get input text
    $password =  $_POST['password'];
    $message = "Username ".$name. ".</br>Password  ".$password." </br> Hah we don't hash";
    echo $message;
  }

?>


</body>
</html>
