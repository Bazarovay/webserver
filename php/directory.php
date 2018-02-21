<html>
  <form name="form1" method="post" action="index.php">
    <tr class="tableheader">
      <td align="center" colspan="2"><input type="submit" name="Home" value="Home"></td>
    </tr>
  </form>

<body>
<head>

<?php
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
printf("<tr><td>Name</td><td colspan=2>Email</td><td colspan=2>General Information</td></tr>\n");

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
}
mysql_close($con);
?>
</table>
</body>
</html>
