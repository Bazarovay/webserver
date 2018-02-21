<?php

$server = "localhost";
$user = "root";
$pass = "changeme";
$db = "webserver";


mysql_connect("$server","$user","$pass") or die('cannot connect');
mysql_select_db("$db")or die("cannot connect");

$username = $_POST['username'];
$password = $_POST['password'];
echo "$username";
echo "$password";
$sql = "Insert into users values ('$username','$password')";
$result = mysql_query($sql);
?>
