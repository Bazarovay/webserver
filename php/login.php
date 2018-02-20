<html>
<body>
<head>
<style type="text/css">
body {
background-image: url('<?php echo $backpic;?>');
}
</style>

<form name="form1" method="post" action="index.php">
<tr class="tableheader">
<td align="center" colspan="2"><input type="submit" name="Home" value="Home"></td>
</tr>
</form>

<form name="form1" method="post" action="checklogin.php">
<tr class="tableheader">
<td align="center" colspan="2"><font size="5" color="black">Enter Login Info:</td></font>
<br>
</tr>
<tr class="tablerow">
<td align="right"><font size="5"color="black">Username</td></font>
<td><input type="text" name="userName"></td>
<br>
</tr>
<tr class="tablerow">
<td align="right"><font size="5"color="black">Password</td></font>
<td><input type="password" name="password"></td>
<br>
</tr>
<tr class="tableheader">
<td align="center" colspan="2"><input type="submit" name="submit" value="Submit"></td>
</tr>
</form>
</body>
</html>
