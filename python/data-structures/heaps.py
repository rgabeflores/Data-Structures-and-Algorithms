import random as r
import time as t
import math as f

DEBUG = False

lower = -10000
upper = 10000

# Node: i
# Left-Child: 2i
# Right-Child: 2i+1

def build_MaxHeap(a):
	n = len(a) - 1
	
	for _ in range(n, -1, -1):
		new_a = max_heapify(a, _)

	return new_a

def max_heapify(a,i):
	left = (2 * i) + 1
	right = (2 * i) + 2
	if right < len(a):
		if a[i] > a[left] and a[i] > a[right]:
			return a
		elif a[left] > a[i] and a[left] > a[right]:
			a[left] += a[i]	
			a[i] = a[left] - a[i]
			a[left] -= a[i]	# Swap Without 3rd Variable
			return max_heapify(a, left)
		else:
			a[right] += a[i]
			a[i] = a[right] - a[i]
			a[right] -= a[i]
			return max_heapify(a, right)
	else:
		if left < len(a):
			if a[i] < a[left]:
				a[left] += a[i]
				a[i] = a[left] - a[i]
				a[left] -= a[i]
				return a
		return a
	
def heap_sort(a):
	b = []
	n = len(a) - 1
	for i in range(n, 0, -1):
		b.insert(0, a[0])
		a[0] = a[i]
		del a[i]
		a = max_heapify(a,0)
		
	return b

def generate_array(n):
	
	print("Generating array... ")

	a = []

	for _ in range(n):
		a.append(r.randint(lower,upper))

	return a

def main():
	print("Assignment 5")
	
	if DEBUG:
		a = [1,7,2,23,5,41]
	else:
		n = int(input("Enter a positive integer: "))
		a = generate_array(n)

		print("\nRandomly generated array: ", a)
		a = build_MaxHeap(a)
		print("\nMax Heap built from array:",a)
		a = heap_sort(a)
		print("\nArray after heapsort:",a)

if __name__ == "__main__":
	main()