import random as r

def binarySearch(mArray, key):
    length = len(mArray)
    if length == 0:
        return False
    elif length == 1:
        if mArray[0] == key:
            return True
        else:
            return False
    else:
        mid = (int)(length / 2)
        if mArray[mid] == key:
            return True
        elif mArray[mid] > key:
            return binarySearch(mArray[:mid], key)
        else:
            return binarySearch(mArray[mid:], key)

def main():

    a = []

    for i in range(100):
        a.append(r.randint(-100,100))

    a.sort()

    n = int(input("Enter a number: "))

    print(binarySearch(a,n))

if __name__ == "__main__":
    main()