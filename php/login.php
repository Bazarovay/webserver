<html>
<body>
<head>
<style type="text/css">
body {
background-image: url('<?php echo $backpic;?>');
}
</style>

<link rel="stylesheet" href="styles/audit.css">

<button id="home" class="button" name="Home" value="Home"> |^| Home </button>

<form name="form1" method="post" action="checklogin.php">
<tr class="tableheader">
<td align="center" colspan="2"><font size="5" color="black">Enter Login Info:</td></font>
<br>
</tr>
<tr class="tablerow">
<td align="right"><font size="5"color="black">Username</td></font>
<td><input type="text" name="username"></td>
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
<form name="form1" method="post" action="signup.html">
<tr class="tableheader">
<td align="center" colspan="2"><input type="submit" name="signup" value="Sign up"></td>
</tr>
</form>

<script src="js/scripts.js"></script>

</body>
</html>
