
public class Search {

	public static boolean binarySearch(int[] a, int key, int lower, int upper) {
		int mid = (lower + upper) / 2;
		if((mid == a.length - 1) || (mid == 0)) {
			if(a[mid] == key) return true;
			else	return false;
		}
		else {
			if(a[mid] > key) return binarySearch(a, key, lower, mid);
			else if(a[mid] < key) return binarySearch(a, key, mid, upper);
			else 	return true;
		}
	}
	public static boolean linearSearch(int[] a, int key) {
		for(int i = 0; i < a.length; i++) {
			if(a[i] == key) return true;
		}
		return false;
	}
}
