public class Reverse{
	public static void main(String[] args){
		String text = "This is some sample text";
		String reverse = reverse(text);
		System.out.println("Before reverse: " + text);
		System.out.println("After reverse: " + reverse);
	}
	public static String reverse(String text){
		if(text.length() <= 1) return text;
		else{
			String last = text.substring(text.length()-1);
			String sub = text.substring(0, text.length()-1);
			return last + reverse(sub);
		}
	}
}