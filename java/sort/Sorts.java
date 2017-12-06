
public class Sorts {
	public static int[] insertionSort(int[] a) {
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
}
