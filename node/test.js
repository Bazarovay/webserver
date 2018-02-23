app.get('/', function(req, res) {
  var name = 'hello';
            res.render("test.html", {name:name});

        });
