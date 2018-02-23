<?php
$server = "localhost";
$user = "root";
$pass = "root";
$db = "webserver";
$user_id = $_GET['id'];

#echo "$user_id";
$link = mysqli_connect("$server","$user","$pass","$db") or die('cannot connect');
// mysql_select_db("$db")or die("cannot connect");

$result = mysqli_query($link, "Select * from users where id='$user_id';");
echo $sql;
$count = mysqli_num_rows($sql);
$result = mysqli_fetch_assoc($link, $sql);
$result2 = $result['name'];
if ($count == 1){
	echo ("The requested id[$user_id] belongs to $result2");
} else {
	echo "Please add a variable to the URI, for example lookup.php?id=1";
}
?>
