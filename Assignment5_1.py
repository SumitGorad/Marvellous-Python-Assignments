def Sum(num1,num2):
    ans = 0
    ans = num1 + num2
    return ans

def Difference(num1,num2):
    ans = 0
    ans = num1 - num2
    return ans

def Product(num1,num2):
    ans = 0
    ans = num1 * num2
    return ans

def Division(num1,num2):
    ans = 0
    ans = num1 / num2
    return ans

def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    a = Sum(no1,no2)
    print("Sum : ",a)
    
    b = Difference(no1,no2)
    print("Difference : ",b)
    
    c = Product(no1,no2)
    print("Product : ",c)

    d = Division(no1,no2)
    print("Division : ",d)
    
if __name__ == "__main__":
    main()