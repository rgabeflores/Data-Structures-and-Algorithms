package powermod;
import java.util.Scanner;

public class PowerMod {
	public static void main(String[] args) {
		int base = 524;
		int exponent = 111555;
		int modulus = 11;
		System.out.printf("Result: %d\n", pmod(base,exponent,modulus));
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