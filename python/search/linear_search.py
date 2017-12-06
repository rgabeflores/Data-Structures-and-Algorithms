import random as r

def linearSearch(mArray, key):
    for _ in mArray:
        if _ == key:
            return True
    return False

def main():

    a = []

    for i in range(100):
        a.append(r.randint(-100,100))

    a.sort()

    n = int(input("Enter a number: "))

    print(linearSearch(a,n))

if __name__ == "__main__":
    main()