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
$sql = "select * from users where username='$username' and password='$password'";
$result = mysql_query($sql);
$check = mysql_num_rows($result);
if ($check == 1){
	session_start();
	$_SESSION['username'] = $username;
	header("Location: login-successful.php");
} else {
	header("Location: login.php");
}
?>
