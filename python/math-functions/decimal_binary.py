'''
	@author Gabriel Flores
	Implementations of binary to decimal and decimal to binary conversions.
	Binary is represented as a boolean array.
'''
import ux

OPTIONS = ["Decimal -> Binary", "Binary -> Decimal"]

def dec_to_bin(x):
	'''
		Takes an integer and constructs a boolean array for the binary representation of the integer.
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
		Takes a boolean array as a binary representation and calculates the integer value.
	'''
	dec = 0
	e = len(binary) - 1
	for i in range(0,len(binary)):
		if(binary[i]):
			dec += 2 ** e
		e -= 1
	return dec

def parse_bin(binary_str):
	'''
		Parses a string of bits into a boolean array.
	'''
	binary = []
	for i in range(0,len(binary_str)):
		if binary_str[i] == "1":
			binary.append(True)
		elif binary_str[i] == "0":
			binary.append(False)
		else:
			print("Invalid binary string. Characters should only be '1' or '0'.")
			break
	return binary

def print_bin(binary):
	for i in binary:
		if i:
			print("1", end="")
		else:
			print("0", end="")
	print("\n")

def main():

	def main_loop():
		choice = ux.get_user_choice(OPTIONS)
		print("\n\n")
		if choice == 1:
			a = int(input("    Enter an integer in decimal: "))
			result = dec_to_bin(a)

			# Output
			print("\n    Decimal:", a, "\n")
			print("\n    Binary: ", end="")
			print_bin(result)
		elif choice == 2:
			a = input("    Enter a binary string: ")
			a_bin = parse_bin(a)
			result = bin_to_dec(a_bin)

			# Output
			print("\n    Binary: ", end="")
			print_bin(a_bin)
			print("\n    Decimal:", result, "\n")

	ux.to_continue(main_loop)

if __name__ == "__main__":
	main()