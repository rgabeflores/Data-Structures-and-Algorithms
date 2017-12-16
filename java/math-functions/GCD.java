package euclid;

import java.util.Scanner;

public class GCD {

	public static void main(String[] args) {
		int a,b;
		
		Scanner sc = new Scanner(System.in);
		try {
			System.out.println("Enter the first integer:");
			a = sc.nextInt();
			System.out.println("Enter the second integer:");
			b = sc.nextInt();
			System.out.printf("The Greatest Common Divisor of %d and %d is %d.\n", a, b, gcd(a,b));
		}catch(Exception e) {
			System.out.println("Invalid Input... ");
		}
		sc.close();
	}
	/**
	 * Gets the greatest common divisor of two integers
	 * @param a the first integer
	 * @param b the second integer
	 * @return the greatest common divisor of the two integers
	 */
	public static int gcd(int a, int b) {
		int rem, x = a, y = b;
		
		while(y != 0) {
			rem = x % y;
			x = y;
			y = rem;
		}
		return x;
	}
}
