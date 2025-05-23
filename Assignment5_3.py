def ChkAge(a):
    if (a >=18) :
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

def main():
    age = int(input("Enter age : "))

    ChkAge(age)

if __name__ == "__main__":
    main()
