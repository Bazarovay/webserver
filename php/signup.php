<?php

$server = "localhost";
$user = "root";
$pass = "root";
$db = "webserver";


// "127.0.0.1", "my_user", "my_password", "my_db")
$link = mysqli_connect("$server","$user",$pass, $db) or die('cannot connect');
// mysqli_select_db("$db")or die("cannot connect");

$username = $_POST['username'];
$password = $_POST['password'];
echo "$username";
echo "$password";
$sql = "Insert into users VALUES (NULL, '$username','$password')";
$result = mysqli_query($link, $sql);
$new_id = mysqli_insert_id($link);
echo $new_id;
?>
