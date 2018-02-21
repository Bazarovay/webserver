<?php
$server = "localhost";
$user = "root";
$pass = "changeme";
$db = "webserver";
$user_id = $_GET['id'];
#echo "$user_id";
mysql_connect("$server","$user","$pass") or die('cannot connect');
mysql_select_db("$db")or die("cannot connect");

$sql = mysql_query("Select * from secret where id='$user_id';");
$count = mysql_num_rows($sql);
$result = mysql_fetch_assoc($sql);
$result2 = $result['name'];
if ($count == 1){
	echo ("The requested id[$user_id] belongs to $result2");
} else {
	echo "Please add a variable to the URI, for example lookup.php?id=1";
}
?>
