'''
	@author Gabriel Flores
	Various mathematical functions concatenated into one script. This script allows
	the user to choose which functions to use.
'''

import check_prime
import decimal_binary
import euclidean_algorithm
import power_mod
import reverse_number


def switch(x):
	exec(str({
		1: check_prime,
		2: decimal_binary,
		3: euclidean_algorithm,
		4: power_mod,
		5: reverse_number
	}[x].main()))

def main():

	options = ["(1) Check Prime", "(2) Decimal/Binary Conversions", "(3) Greatest Common Divisor", "(4) Power Mod Calculation", "(5) Reverse Integer"]

	ui_menu = "\n    "

	for option in options:
		ui_menu += option + "\n    "

	cont = True

	while cont:
		while True:
			try:
				print(ui_menu)
				choice = int(input("Enter a function to use:  "))
				if choice <= len(options) and choice > 0:
					break
				else:
					raise ValueError("Number too large.")
			except ValueError as e:
				print("\n\n    Please enter a valid choice.\n")
				continue

		print("\n\n")
		switch(choice)

		while True:
			again = input("Would you like to use another function? (Y/N)\n")
			if again.upper() == "Y":
				break
			elif again.upper() == "N":
				cont = False
				break
			else:
				print("\n\n    Please enter a valid option.\n")
				continue

	print("\n\n")


if __name__ == "__main__":
	main()