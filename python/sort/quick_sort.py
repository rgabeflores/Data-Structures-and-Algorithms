import random as r

def quick_sort(a):
	if(len(a) >= 3):
		pivot = get_pivot(a)

		left = list()
		right = list()
		equal = list()

		for x in a:
			if x < pivot:
				left.append(x)
			elif x > pivot:
				right.append(x)
			else:
				equal.append(x)

		return quick_sort(left) + equal + quick_sort(right)
	elif(len(a) == 2):
		if a[0] < a[1]:
			return a
		else:
			return [a[1],a[0]]
	else:
		return a

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
	n = int(input("Enter a positive integer: "))

	a = []

	for _ in range(n):
		a.append(r.randint(-7000,7000))

	print(a)
	
	print(quick_sort(a))
	
if __name__ == '__main__':
	main()