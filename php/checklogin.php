<?php
// include $argv[1];
// var_dump($_POST)
$server = "localhost";
$user = "root";
$pass = "root";
$db = "webserver";
$username = $_POST['username'];
$password = $_POST['password'];
echo "$username";
echo "$password";

$link = mysqli_connect("$server","$user","$pass","$db") or die('cannot connect');
// mysqli_select_db("$db")or die("cannot connect");

$sql = "select * from users where username='$username' and password='$password'";
$result = mysqli_query($link, $sql);

if ($result == True) {
  session_start();
  $_SESSION['username'] = $username;
  header("Location: login-successful.php");
} else {
	header("Location: login.php");
}
?>
