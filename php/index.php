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
    font-size: 16px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    margin-left: 10%;
    margin-top: 10px;
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

<button id="login" class="button" name="Login" value="Login">Login</button>

<button id="directory" class="button" name="Login" value="Directory">Directory</button>

<button id="lookup" class="button" name="lookup" value="lookup">Lookup</button>



<script>

var btn = document.getElementById('home');
console.log(btn);
if(btn){
  btn.addEventListener('click', function() {
    document.location.href = 'index.php';
  });
}

var btn = document.getElementById('login');
console.log(btn);
if(btn){
  btn.addEventListener('click', function() {
    document.location.href = 'login.php';
  });
}

var btn = document.getElementById('directory');
console.log(btn);
if(btn){
  btn.addEventListener('click', function() {
    document.location.href = 'directory.php';
  });
}

var btn = document.getElementById('lookup');
console.log(btn);
if(btn){
  btn.addEventListener('click', function() {
    document.location.href = 'lookup.php';
  });
}
</script>


</body>
</html>
