

def reverse_num(num):
	final = 0

	while(num != 0):
		r = num % 10
		num = int(num / 10)
		final = (final * 10) + r

	return final

def main():
	a = int(input("Enter an integer to reverse: "))

	print("Original", a)

	a = reverse_num(a)

	print("Reversed", a)

if __name__ == "__main__":
	main()