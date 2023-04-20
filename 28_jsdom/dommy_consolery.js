// Team Soeckies :: Shreya Roy, Maya Nelson
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-19
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
const j = 20;



//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };



var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};
	//no return statement returns undefined in console

	// index n is removed starting from zero (despite browser starting from 1)
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};
	//cant "reassign" colors if element already has a color class on it

//insert your implementations here for...
//FAC
var fac = function(n) {
	if (n < 2) 
        return 1;
      else {
          return (n * fac(n - 1));
      }
}

//FIB
var fib = function(n){

  if (n <= 1){
	  return n
  }
  return fib(n-1)+fib(n-2);
}

// GCD
var gcd = function(n0,n1){
	while(!(n0 % n1 == 0)){
		var f = n0 % n1;
		n0 = n1;
		n1 = f;
	}		
	return n1;
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  return param1+param2;
};

	// arrow syntax does not use function keyword but seems to act the same as a variable assigned to a function
	// calling the variable myFxn instead of the function myFxn() returns the contents of the function
	// Q: Const vs var ?

const testAll = () => {
	return "6th Fib: " + fib(6) + ". 6!: " + fac(6) + ". GCD of 24 and 18: " + gcd(24,18)
	
};


addItem(testAll())

var button = document.getElementById("fib"); 
button.addEventListener('click', ()=>{
	document.getElementById("fibR").innerHTML = fib(15)
}
);

var button = document.getElementById("fac"); 
button.addEventListener('click', ()=>{
	document.getElementById("facR").innerHTML = fac(6)
}
);

var button = document.getElementById("gcd"); 
button.addEventListener('click', ()=>{
	document.getElementById("gcdR").innerHTML = gcd(24, 18)
}
);
