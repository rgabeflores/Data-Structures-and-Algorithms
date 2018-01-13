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
import statistics
import ux

OPTIONS = ["Check Prime", "Decimal/Binary Conversions", "Greatest Common Divisor", "Power Mod Calculation", "Reverse Integer", "Data Set Statistics"]

def switch(x):
	exec(str({
		1: check_prime,
		2: decimal_binary,
		3: euclidean_algorithm,
		4: power_mod,
		5: reverse_number,
		6: statistics
	}[x].main()))

def main():

	def main_loop():
		choice = ux.get_user_choice(OPTIONS)

		print("\n\n")
		switch(choice)

	ux.to_continue(main_loop)


if __name__ == "__main__":
	main()