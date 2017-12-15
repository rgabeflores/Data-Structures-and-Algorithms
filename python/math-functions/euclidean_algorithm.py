
# Euclidean Algorithm to find the Greatest Common Divisor
def gcd(a,b):
	x = a
	y = b
	while y != 0:
		r = x % y
		x = y
		y = r
	return x

def main():

	a = int(input("Enter the first number: "))
	b = int(input("Enter the second number: "))

	x = gcd(a, b)
	print("\nThe GCD of,", a, "&", b, "is:", x, "\n")

if __name__ == "__main__":
	main()