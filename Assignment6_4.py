def Fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Factorial of",n, "is : ", factorial)
            
def main():
    print("Enter a number:")
    num = int(input())
    Fact(num)

if __name__ == "__main__":
    main()
