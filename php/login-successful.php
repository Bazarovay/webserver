<?php
session_start();

if(isset($_SESSION['username'])){
	header("location:login.php");
}
?>

<html>
<body>
<h2>Company Image Gallery</h2>
<a href="logout.php">Logout</a>
</body>
</html>
