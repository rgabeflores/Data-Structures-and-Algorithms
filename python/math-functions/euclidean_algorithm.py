'''
	@author Gabriel Flores
	Gets the greatest common divisor using the Euclidean Algorithm.
'''

def gcd(a,b):
	'''
		Uses the Euclidean Algorithm to get the
		greatest common divisor of two numbers.
	'''
	x = a
	y = b
	while y != 0:
		r = x % y
		x = y
		y = r
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
			a = int(input("    Enter the first number: "))
			b = int(input("    Enter the second number: "))
			x = gcd(a, b)

			# Output
			print("\nThe GCD of,", a, "&", b, "is:", x, "\n")
		except ValueError as e:
			print("\n\n    Please enter a valid choice.\n")
			continue

		cont = to_continue()

	

if __name__ == "__main__":
	main()