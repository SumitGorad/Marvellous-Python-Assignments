def main():
    num = int(input("Enter a number you want : "))
    
    power_of_two = lambda x: 2 ** x

    ret = power_of_two(num)
    print("Output:", ret)

if __name__ == "__main__":
    main()
