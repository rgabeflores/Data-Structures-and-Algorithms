def dec_to_bin(x):
	binary = []

	half = int(x / 2)
	i = 0

	while 2 ** i <= half:
		i += 1
		
	while i >= 0:
		if(x - (2 ** i)) >= 0:
			x -= 2 ** i
			binary.append(True)
		else:
			binary.append(False)
		
		i -= 1

	return binary

def pmod(b,e,m):
	e_bin = dec_to_bin(e)
	
	x = 1
	power = b % m

	for i in range(len(e_bin)-1, -1, -1):
		if e_bin[i]:
			x = (x * power) % m
		power = (power ** 2) % m

	return x

def main():
	b = int(input("Enter b: "))
	e = int(input("Enter e: "))
	m = int(input("Enter m: "))

	result = pmod(b, e, m)
	print("\n",result,"\n")

if __name__ == "__main__":
	main()