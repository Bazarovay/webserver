<html>
 <head>
 </head>
<body>
<head>


<style type="text/css">

body {
    background-color: lightblue;
}

#header {
    background: #ff7f7f;
    height: 20%;
}
h1{
    background: orange;
    margin-top:10px;
    margin-left: 35%;
    margin-right: 30%;
}

.button {
    background-color: orange;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
}
.button:hover {
    background-color: red;
    color: white;
}

</style>



</head>

    <div id="header">
     <h1>Our Vulnerable PHP Webapp</h1>
    </div>


</tr>

<button id="home" class="button" name="Home" value="Home"> |^| Home </button>


<form name="form4" method="post" action="login.php">
</tr>
<tr class="tableheader">
<td align="center" colspan="2">
  <input class="button"  type="submit" name="Login" value="Login"></td>
</tr>
</form>


<form name="form5" method="post" action="directory.php">
</tr>
<tr class="tableheader">
<td align="center" colspan="2">
  <input class="button" type="submit" name="Directory" value="Directory"></td>
</tr>
</form>


<form name="form6" method="post" action="lookup.php">
</tr>
<tr class="tableheader">
<td align="center" colspan="2">
  <input class="button" type="submit" name="lookup" value="Lookup ID"></td>
</tr>
</form>


<script>

var btn = document.getElementById('home');
console.log(btn);
if(btn){
  btn.addEventListener('click', function() {
    document.location.href = 'index.php';
  });
}
</script>


</body>
</html>
