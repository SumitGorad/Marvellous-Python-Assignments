import MarvellousNum

def ListPrime(l):
    sumofPrime = 0
    for i in l:
        if MarvellousNum.ChkPrime(i):
            sumofPrime = sumofPrime + i

    print("Addition of prime numbers is : ", sumofPrime)

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = []

    print("Enter the values : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    print("Entered elements are : ")
    for value in data:
        print(value)

    ListPrime(data)

if __name__ == "__main__":
    main()