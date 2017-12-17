
public class Sorts {
	public static int[] selectionSort(int[] a) {
		for(int i = 0; i < a.length; i++) {
			for(int j = i + 1; j < a.length; j++) {
				if (a[i] <= a[j]) continue;
				else {
					a[i] += a[j];
					a[j] = a[i] - a[j];
					a[i] -= a[j];
				}
			}
		}
		return a;
	}
	public static int[] insertionSort(int[] a) {
		int temp, j;
		for(int i = 1; i < a.length; i++) {
			temp = a[i];
			j = i;
			while(j > 0 && temp < a[j - 1]) {
				a[j] = a[j-1];
				j--;
			}
			a[j] = temp;
		}
		return a;
	}
}
