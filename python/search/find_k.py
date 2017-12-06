import random as r

def find_k(a,key):

	pivot = get_pivot(a)
	left = list()
	right = list()

	for x in a:
		if x <= pivot:
			left.append(x)
		else:
			right.append(x)

	length = len(left)
	if(length > key):
		return find_k(left,key)
	elif(length == key):
		return pivot
	else:
		return find_k(right, (key - (len(left))))

def get_pivot(a):
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

def main():

	n = int(input("\nEnter a positive integer: "))

	a = []

	for _ in range(n):
		a.append(r.randint(-100,100))

	print(a)

	k = int(input("\nEnter a number between 1 and %d: " % n))

	print("The " + str(k) + "th element is " + str(find_k(a,k)))

if __name__ == "__main__":
	main()