package powermod;

public class DecimalBinary {
	public static boolean[] decToBin(int num) {
		int half = (int) num / 2, i = 0;
		
		while((int)Math.pow(2, i) <= half)
			i++;
		
		boolean[] bin = new boolean[i+1];
		
		for(int j = 0; i >= 0; i--, j++) {
			if(num - (int)Math.pow(2, i) >= 0) {
				num -= (int)Math.pow(2, i);
				bin[j] = true;
			}
			else
				bin[j] = false;
		}
		
		return bin;
	}
	public static int binToDec(boolean[] bits) {
		int decimal = 0;
		int e = bits.length - 1;
		for(boolean bit: bits) {
			if(bit)
				decimal += (int) Math.pow(2, e);
			e--;
		}
		return decimal;
	}
	public static void printBin(boolean[] bits) {
		for(boolean bit: bits)
			if(bit) 
				System.out.print("1");
			else 
				System.out.print("0");
		System.out.println();
	}
}
