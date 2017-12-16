package prime;

import java.util.Scanner;
public class CheckPrime {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		try {
			System.out.println("Enter an integer to check if it is prime:");
			int num = sc.nextInt();
			if(isPrime(num))
				System.out.printf("%d is a prime number.\n", num);
			else
				System.out.printf("%d is not a prime number.\n", num);
		}catch(Exception e) {
			System.out.println("Invalid value entered.");
		}
		
		sc.close();
	}
	/**
	 * Checks whether an integer is prime or not.
	 * @param x the possible prime number
	 * @return whether or not an integer is prime
	 */
	public static boolean isPrime(int x) {
		double sqrt = Math.sqrt(x);
		for(int i = 2; i < sqrt; i++)
			if(x % i == 0) return false;
		return true;
	}
}
