'''
	@author Gabriel Flores
	A modular expression calculator that implements modular exponentiation.
'''

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

def pmod(b,e,m):
	'''
		Uses modular exponentiation to calculate modular expressions with large values
	'''
	e_bin = dec_to_bin(e)
	
	x = 1
	power = b % m

	for i in range(len(e_bin)-1, -1, -1):
		if e_bin[i]:
			x = (x * power) % m
		power = (power ** 2) % m

	return x

def to_continue():
	while True:
		again = input("    Would you like to try again? (Y/N) ")
		if again.upper() == "Y":
			return True
		elif again.upper() == "N":
			return False
		else:
			print("\n\n    Please enter a valid option.\n")
			continue

def main():

	cont = True

	while cont:
		try:
			print("\n\n")
			print("\n        Format:    \n")
			print("        b^e mod m    \n")

			b = int(input("    Enter b: "))
			e = int(input("    Enter e: "))
			m = int(input("    Enter m: "))

			result = pmod(b, e, m)
			print("\n    Result:",result,"\n")
		except ValueError as e:
			print("\n\n    Please enter a valid choice.\n")
			continue

		cont = to_continue()

	print("\n\n")

if __name__ == "__main__":
	main()