import sys

def rot13(text):
	shift = ""
	for _ in text:
		key = ord(_)
		if key >= ord('a') and key <= ord('m'):
			key += 13
		elif key >= ord('A') and key <= ord('M'):
			key += 13
		elif key >= ord('n') and key <= ord('z'):
			key -= 13
		elif key >= ord('n') and key <= ord('z'):
			key -= 13
		shift += chr(key)
	return shift
           
def main():
	if len(sys.argv) > 1:
		print(rot13(sys.argv[1]))
	else:
		x = str(input("Enter a string to encode or decode: "))
		print(rot13(x))


if __name__ == "__main__":
	main()