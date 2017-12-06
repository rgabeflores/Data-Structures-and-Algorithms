
function linearSearch(arr, key){
	for(var i = 0; i < arr.length; i++){
		if(arr[i] === key){
			return true;
		}
	}
	return false;
}

var test = [0, 2, 12, 13, 9, 22];

console.log(linearSearch(test, 54));