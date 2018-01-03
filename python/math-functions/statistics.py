import random as r
import re

options = ["(1) Test Random Numbers", "(2) Input Values"]

def mean(a):
	'''
		Gets the average of an array of numbers.
	'''

	total = 0

	for i in a:
		total += i

	return total / len(a)

def median(a, key=None):
	'''
		Implements Divide & Conquer technique to find the middle element of an array.
	'''
	pivot = get_pivot(a)
	left = list()
	right = list()

	if key is None:
		key = int(len(a) / 2)

	for x in a:
		if x <= pivot:
			left.append(x)
		else:
			right.append(x)

	length = len(left)
	if(length > key):
		return median(left,key)
	elif(length == key):
		return pivot
	else:
		return median(right, (key - (len(left))))

def get_pivot(a):
	'''
		Gets the median of the first, middle, and last elements of an unsorted array.
	'''
	first = a[0]
	last = a[len(a) - 1]
	mid = a[int(len(a) / 2)]

	if (first < mid and mid < last) or (last < mid and mid < first):
		return mid
	elif (mid < first and first < last) or (last < first and first < mid):
		return first
	elif (first < last and last < mid) or (mid < last and last < first):
		return last
	else:
		return mid

def mode(a):
	'''
		Finds the most commonly recurring element in an array.
		Returns None if there is no element with more than one isntance.
	'''
	totals = {"_" : 0}

	for i in a:
		if i in totals:
			totals[i] += 1
		else:
			totals[i] = 1

	temp = "_"

	for key in totals:
		if totals[key] > totals[temp]:
			temp = key

	if totals[temp] > 1:
		return temp
	else:
		return None


def std_dev(a, average=None, variance=None):
	'''
		Finds the the standard deviation of elements in an array.
	'''
	if average is None:
		average = mean(a)
	if variance is None:
		variance = variance(a, average)

	return variance ** 0.5

def variance(a, average=None):
	if average is None:
		average = mean(a)

	total = 0
	for i in a:
		total += (average - i) ** 2

	return total / len(a)

def get_user_choice():

	ui_menu = "\n    "

	for option in options:
		ui_menu += option + "\n    "

	while True:
		try:
			print(ui_menu)
			choice = int(input("    Enter a function to use:  "))
			if choice <= len(options) and choice > 0:
				return choice
			else:
				raise ValueError("Number too large.")
		except ValueError as e:
			print("\n\n    Please enter a valid choice.\n")
			continue


def to_continue():
	while True:
		again = input("Would you like to try again? (Y/N)\n")
		if again.upper() == "Y":
			return True
		elif again.upper() == "N":
			return False
		else:
			print("\n\n    Please enter a valid option.\n")
			continue

def randomTest():

	n = int(input("    Enter the size of the list to test: "))
	
	values = [r.randint(0,100) for i in range(n)]
	print("\n    Values:", values,"\n")


	_mean = mean(values)
	_median = median(values)
	_mode = mode(values)
	_variance = variance(values, average=_mean)
	_std_dev = std_dev(values, average=_mean, variance=_variance)

	print("    Mean:", _mean)
	print("    Median:", _median)
	print("    Mode:", _mode)
	print("    Variance:", _variance)
	print("    Standard Deviation:", _std_dev)


def userInputTest():

	user_input = input("    Enter the values separated by commas or spaces: ")

	values = [int(x.strip()) for x in re.split(' |, |\n', user_input)]
	print("\n    Values:", values,"\n")


	_mean = mean(values)
	_median = median(values)
	_mode = mode(values)
	_variance = variance(values, average=_mean)
	_std_dev = std_dev(values, average=_mean, variance=_variance)

	print("    Mean:", _mean)
	print("    Median:", _median)
	print("    Mode:", _mode)
	print("    Variance:", _variance)
	print("    Standard Deviation:", _std_dev)


def main():

	cont = True

	while cont:
		
		choice = get_user_choice()

		print("\n")
		
		if choice == 1:
			randomTest()
		elif choice == 2:
			userInputTest()

		print("\n\n")

		cont = to_continue()

	print("\n\n")

if __name__ == "__main__":
	main()