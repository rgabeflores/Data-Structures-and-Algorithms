package powermod;
import java.util.Scanner;

public class PowerMod {
	public static void main(String[] args) {
		int base, exponent, modulus;
		Scanner sc = new Scanner(System.in);
		try {
			System.out.println("Enter the base: ");
			base = sc.nextInt();
			System.out.println("Enter the exponent: ");
			exponent = sc.nextInt();
			System.out.println("Enter the modulus: ");
			modulus = sc.nextInt();
			System.out.printf("Result: %d\n", pmod(base,exponent,modulus));
		}catch(Exception e) {
			System.out.println("Input was invalid or there was an error.");
		}
	}
	/**
	 * Calculates large modular expressions efficiently
	 * @param b integer value
	 * @param e exponent of integer
	 * @param m value to mod
	 * @return the value of the mod expression
	 */
	public static int pmod(int b, int e, int m) {
		boolean[] bin = DecimalBinary.decToBin(e);
		
		int x = 1;
		int power = b % m;
		
		for(int i = bin.length - 1; i >= 0; i--) {
			if(bin[i])
				x = (x * power) % m;
			power = (power * power) % m;
		}
		return x;
	}
}