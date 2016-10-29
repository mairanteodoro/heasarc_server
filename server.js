//start.js

// require/import the HTTP module
var http = require('http');
// define a port to listen to
const PORT = 3000;

// function to handle requests and send response
function handleRequest(request, response, next){
  var userData = [1,2,3,4,5,6,7,8,9];// request.query.data;
  // call Python script
  let spawn = require('child_process').spawn,
      py    = spawn('python', ['./python/script.py']),
      dataString = '';

  // provide data to the script
  py.stdout.on('data', function(data){
    dataString += data.toString();
  });
  // after finishing up the Pythons script,
  // return the http response to the user
  py.stdout.on('end', function(){
    // set CORS headers
  	response.setHeader('Access-Control-Allow-Origin', '*');
  	response.setHeader('Access-Control-Request-Method', '*');
  	response.setHeader('Access-Control-Allow-Methods', 'OPTIONS, GET');
  	response.setHeader('Access-Control-Allow-Headers', '*');
    // write <head> metadata
    response.writeHead(200, {"Content-Type": "application/json"});
    // deliver content to user
    response.end(JSON.stringify({'data': userData, 'result': dataString}));
  });

  py.stdin.write(JSON.stringify(userData));
  py.stdin.end();
}

// create a server
var server = http.createServer(handleRequest);

// start server
server.listen(PORT, function(){
    // callback triggered when server is successfully listening
    console.log("Server listening on: http://localhost:%s", PORT);
});
