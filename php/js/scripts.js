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
