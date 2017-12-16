function isPrime(x){
	var square_root = Math.sqrt(x);
	for(var i = 2; i < square_root; i++){
		if(x % i == 0) {
			return false;
		}
	}
	return true;
}

var a = 7;
var b = 24;

console.log("Is " + a + " prime? " + isPrime(a));
console.log("Is " + b + " prime? " + isPrime(b));