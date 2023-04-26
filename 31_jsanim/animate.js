var c = document.getElementById("playground");// GET CANVAS
var dotButton = document.getElementById("buttonCircle"); // GET DOT Button
var stopButton = document.getElementById("buttonStop");// GET STOP BUTTON 

var ctx = c.getContext("2d"); // YOUR CODE HERE

ctx.fillStyle = "blue"// YOUR CODE HERE

var requestID;  // int global var for use with animation frames

var clear = (e) => {
  //console.log("wiping canvas...")
  ctx.clearRect(0,0,c.clientWidth,c.clientHeight)
};

var radius = 0;
var growing = true;

var drawDot = () => {
  clear();

  ctx.beginPath();
  ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();
  
  if (radius > 250 && growing){
	  growing = false;
  }
  else if (radius-1 < 0 && !growing) {
	  growing = true;
  }
  
  if(growing){
	  radius += 1;
  }
  else {
	  radius -= 1;
  }
  
  window.cancelAnimationFrame(requestID);
  requestID = window.requestAnimationFrame(drawDot);
};

//var stopIt = function() {
var stopIt = () => {
	console.log("stopIt invoked...")
	console.log( requestID );
	window.cancelAnimationFrame(requestID);
	
	
};

dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click", stopIt );
