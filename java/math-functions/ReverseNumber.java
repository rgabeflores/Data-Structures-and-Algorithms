package reversenum;

import java.util.Scanner;

public class ReverseNumber {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		try {
			System.out.println("Enter an integer to get its digits reversed:");
			int num = sc.nextInt();
			System.out.println();
			System.out.println("Original number: ");
			System.out.println(num);
			System.out.println("Result:");
			System.out.println(reverseNumber(num));
			
		}catch(Exception e) {
			System.out.println("Invalid value entered.");
		}
		
		sc.close();
	}
	
	public static int reverseNumber(int num) {
		int result = 0, remainder;
		
		while(num != 0) {
			remainder = num % 10;
			num = (int) num / 10;
			result = (result * 10) + remainder;
		}
		
		return result;
	}
}
