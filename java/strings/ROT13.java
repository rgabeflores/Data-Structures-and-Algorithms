public class ROT13{
	public static void main(String[] args){
		String text = "This is some sample text";
		String rot13 = rot13(text);
		System.out.println("Before ROT13 shift: " + text);
		System.out.println("After ROT13 shift: " + reverse);
	}
	public static String rot13(String text){
		String shift = "";
		for (int i = 0; i < text.length(); i++) {
			char c = text.charAt(i);
			if       (c >= 'a' && c <= 'm') c += 13;
			else if  (c >= 'A' && c <= 'M') c += 13;
			else if  (c >= 'n' && c <= 'z') c -= 13;
			else if  (c >= 'N' && c <= 'Z') c -= 13;
			shift += c;
		}
		return shift;
	}
}