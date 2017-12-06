import random as r

def insertion_sort(_list):
    for i in range(0, len(_list) - 1):
        for j in range(i + 1,len(_list)):
	        if _list[i] <= _list[j]:
	        	continue
	        else:
	        	_list[j] = _list[j] + _list[i]
	        	_list[i] = _list[j] - _list[i]
	        	_list[j] = _list[j] - _list[i]

    return _list

def main():
	n = int(input("Enter a positive integer: "))

	a = []
	
	for _ in range(n):
		a.append(r.randint(-7000,7000))

	print(a)

	print(insertion_sort(a))
	
if __name__ == '__main__':
	main()