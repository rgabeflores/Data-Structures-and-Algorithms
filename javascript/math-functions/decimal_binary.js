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
function binToDecimal(binary){
	var decimal = 0;
	for(var i = 0, e = binary.length - 1; i <= binary.length; i++, e--){
		if(binary[i] == true){
			decimal += parseInt(Math.pow(2, e));
		}
	}
	return decimal;
}
function printBin(binary){
	var bin = "";
	for(var i = 0; i <= binary.length; i++){
		if(binary[i] == true){
			bin += "1";
		}
		else{
			bin += "0";
		}
	}
	console.log(bin);
}

var x = 142;
var bin = decToBin(x);
var reverse = binToDecimal(bin);
console.log(x);
console.log(bin);
console.log(reverse);
printBin(bin);