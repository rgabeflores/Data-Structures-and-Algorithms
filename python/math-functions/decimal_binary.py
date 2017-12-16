
def dec_to_bin(x):
	binary = []

	base = 2
	half = int(x / 2)
	i = 0

	while base ** i <= half:
		i += 1
		
	while i >= 0:
		if(x - (base ** i)) >= 0:
			x -= base ** i
			binary.append(True)
		else:
			binary.append(False)
		
		i -= 1

	return binary

def bin_to_dec(binary):
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