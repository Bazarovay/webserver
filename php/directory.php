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

while ($row){
echo "<tr>";
echo "<td>".$row['name']."</td>";
echo "<td>".$row['email']."</td>";
echo "<td>".$row['general_information']."</td>";
echo "</tr>";
$row=mysql_fetch_assoc($sql);
#$row_id=$row['id'];
}
echo "after while";
mysql_close($con);
?>
</table>
</body>
</html>
