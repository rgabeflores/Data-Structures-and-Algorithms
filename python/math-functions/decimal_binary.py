def dec_to_bin(x):
	'''
		Takes an integer and constructs a boolean array for the binary representation of the integer
	'''
	binary = []

	half = int(x / 2)
	i = 0

	while 2 ** i <= half:
		i += 1
		
	while i >= 0:
		if(x - (2 ** i)) >= 0:
			x -= 2 ** i
			binary.append(True)
		else:
			binary.append(False)
		
		i -= 1

	return binary

def bin_to_dec(binary):
	'''
		Takes a boolean array as a binary representation and calculates the integer value
	'''
	dec = 0
	e = len(binary) - 1
	for i in range(0,len(binary)):
		if(binary[i]):
			dec += 2 ** e
		e -= 1
	return dec

def print_bin(binary):
	for i in binary:
		if i:
			print("1", end="")
		else:
			print("0", end="")
	print("\n")

def main():
	a = int(input("Enter an integer in decimal: "))
	print("\nDecimal:", a, "\n")
	a_bin = dec_to_bin(a)
	print("\nBinary:", a_bin, "\n")
	a_bin_a = bin_to_dec(a_bin)
	print("\nDecimal:", a_bin_a, "\n")
	print_bin(a_bin)

if __name__ == "__main__":
	main()