def main():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    multiply = lambda x, y: x * y

    ret = multiply(num1, num2)
    print("Multiplication of num1 * num2 is :", ret)

if __name__ == "__main__":
    main()
