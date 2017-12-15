function gcd(a,b){
	var x = a;
	var y = b;

	while(y != 0){
		r = x % y;
		x = y;
		y = r;
	}

	return x
}

a = 2133
b = 1455

x = gcd(a, b)

console.log("\nThe Greatest Common Divisor of " + a + " & " + b + " is " + x + "\n");