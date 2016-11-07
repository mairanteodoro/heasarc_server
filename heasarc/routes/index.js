var express = require('express');
var router = express.Router();

/* GET home page (no request for data) */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

/* GET energy converter with params encoded in the address */
/* HOW TO TEST FOR EXISTENCE OF ENCODED PARAM? */
router.get('/conv-energy/:data1/:unit1/:unit2', function(req, res, next) {
  let userValue1 = req.params.data1;
  let userUnit1 = req.params.unit1;
  let userUnit2 = req.params.unit2;
  let data = [Number(userValue1), userUnit1, userUnit2];
  let spawn = require('child_process').spawn;
  let py = spawn('python', ['../python/convEnergy.py']);
  let dataString = '';

  // do this while the process is outputting
  py.stdout.on('data', function(data) {
    dataString += data.toString();
  });
  // do this when process ends
  py.stdout.on('end', function() {
    // deliver data to user
    res.send({'data1': Number(userValue1),
              'unit1': userUnit1,
              'unit2': userUnit2,
              'result': dataString});
  });

  // pass the data to the process
  py.stdin.write(JSON.stringify(data));
  // finish the process
  py.stdin.end();
});

module.exports = router;
