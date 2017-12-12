import sys

def reverse(text):
	# 
	# Recursive 
	# length = len(text)
	# if length <= 1:
	# 	return text
	# else:
	# 	return text[length - 1] + reverse(text[:length - 1])
	# 
	return text[::-1]

def main():
	if len(sys.argv) > 1:
		print(reverse(sys.argv[1]))
	else:
		x = str(input("Enter a string to encode or decode: "))
		print(reverse(x))

if __name__ == "__main__":
	main()