'''
	@author Gabriel Flores
	Reverses the digits of an integer.
'''

def reverse_num(num):
	'''
		Takes an integer and returns the integer with reversed digits
	'''
	final = 0

	while(num != 0):
		r = num % 10
		num = int(num / 10)
		final = (final * 10) + r

	return final

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
			a = int(input("    Enter an integer to reverse: "))
			_a = reverse_num(a)
			# Output
			print("\n    Original", a)
			print("    Reversed", _a)
			print("\n")

		except ValueError as e:
			print("\n\n    Please enter a valid choice.\n")
			continue

		cont = to_continue()

	print("\n\n")

if __name__ == "__main__":
	main()