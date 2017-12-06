function binarySearch(arr, key){
	var mid = Math.floor(arr.length / 2);
	if(mid === 0){
		if(arr[mid] === key){
			return true;
		}
		else{
			return false;
		}
	}
	else{
		if(arr[mid] > key){
			return binarySearch(arr.splice(0, mid), key);
		}
		else if(arr[mid] < key){
			return binarySearch(arr.splice(mid, arr.length), key);
		}
		else{
			return true;
		}
	}
}

var test = [0, 2, 9, 12, 13, 22, 23, 25, 29, 34, 54];

console.log(binarySearch(test, 0));