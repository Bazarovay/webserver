<html>
  <form name="form1" method="post" action="index.php">
    <tr class="tableheader">
      <td align="center" colspan="2"><input type="submit" name="Home" value="Home"></td>
    </tr>
  </form>

<body>
<head>

<?php
$server = "localhost";
$user = "root";
$pass = "changeme";
$db = "webserver";


mysql_connect("$server","$user","$pass") or die('cannot connect');
mysql_select_db("$db")or die("cannot connect");

$sql = mysql_query("Select * from Employees;");
$row=mysql_fetch_assoc($sql);

printf("<!DOCTYPE html>");
printf("<html>");
printf("<head>");
printf("<style>");
printf("table, th, td {");
printf("    border: 1px solid black;");
printf("}");
printf("</style>");
printf("</head>");
printf("<body>");
printf("Employee Directory");


printf("<table border=1>\n");
printf("<tr><td>Name</td><td colspan=1>Email</td><td colspan=1>General Information</td></tr>\n");

<<<<<<< HEAD
$con = mysql_connect("localhost","root","changeme") or die("cannot connect");
$db_select = mysql_select_db('Company',$con);
$result = mysql_query($con, "Select * from Employees");

while ($row=mysql_fetch_assoc($result)){
  echo "<tr>";
  echo "Testing";
  echo "<td>".$row['Name']."</td>";
  echo "<td>".$row['Email']."</td>";
  echo "<td>".$row['General_Information']."</td>";
  echo "</tr>";
=======
while ($row){
echo "<tr>";
echo "<td>".$row['name']."</td>";
echo "<td>".$row['email']."</td>";
echo "<td>".$row['general_information']."</td>";
echo "</tr>";
$row=mysql_fetch_assoc($sql);
#$row_id=$row['id'];
>>>>>>> 14896d78f622f075d1e12b23e04b22ecb7038640
}
echo "after while";
mysql_close($con);
?>
</table>
</body>
</html>
