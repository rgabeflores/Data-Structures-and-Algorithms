'''
	@author Gabriel Flores
	Gets the greatest common divisor using the Euclidean Algorithm.
'''
import ux

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

def main():

	def main_loop():
		try:
			print("\n\n")
			a = int(input("    Enter the first number: "))
			b = int(input("    Enter the second number: "))
			x = gcd(a, b)

			# Output
			print("\nThe GCD of,", a, "&", b, "is:", x, "\n")
		except ValueError as e:
			print("\n\n    Please enter a valid choice.\n")

	ux.to_continue(main_loop)

if __name__ == "__main__":
	main()