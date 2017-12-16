import random as r

def insertion_sort(a):
	for i in range(1,len(a)):
		temp = a[i]
		j = i
		while j > 0 and temp < a[j - 1]: 
			a[j] = a[j - 1]
			j -= 1
		a[j] = temp

	return a

def main():
	n = int(input("Enter a positive integer: "))

	a = []
	
	for _ in range(n):
		a.append(r.randint(-7000,7000))

	print(a)

	print(insertion_sort(a))
	
if __name__ == '__main__':
	main()