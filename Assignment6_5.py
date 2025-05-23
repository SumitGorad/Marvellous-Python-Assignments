def ChkPrime(no):
    if no <= 1:
        return False
    for n in range(2,no):
        if no % n == 0:
            return False
        if no == 2:
            return True
    return True
            
def main():
    print("Enter a number:")
    num = int(input())
    a = ChkPrime(num)
    if a:
        print(num , " is a prime number")
    else:
        print(num , " is not a prime number")

if __name__ == "__main__":
    main()
