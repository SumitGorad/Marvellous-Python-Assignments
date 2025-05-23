def ChkAge(no):
    if (no % 2 == 0) :
        print(no , "is an even number")
    else:
        print(no , "is an odd number")

def main():
    num = int(input("Enter a number : "))

    ChkAge(num)

if __name__ == "__main__":
    main()