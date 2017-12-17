function decToBin(num){
	var binary = [];

	var half = parseInt(num / 2);
	var i = 0;

	while(Math.pow(2, i) <= half){ i++; }

	while(i >= 0){
		if(num - (Math.pow(2,i)) >= 0){
			num -= Math.pow(2,i);
			binary.push(true);
		}
		else{
			binary.push(false);
		}
		i--;
	}
	return binary;
}
function pMod(b, e, m){
	var eBin = decToBin(e);

	var x = 1;
	var power = b % m;

	for(var i = eBin.length - 1; i >= 0; i--){
		if(eBin[i]){
			x = (x * power) % m;
		}
		power = (Math.pow(power, 2)) % m;
	}

	return x;
}

var a = 123;
var b = 33;
var c = 12;

var result = pMod(a, b, c);
console.log(result);