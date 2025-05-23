def MaxNumBet5(l):
    maxn = l[0]
    for i in range(1,len(l)):
        if l[i] > maxn:
            maxn = l[i]

    print("Maximum number is : ", maxn)

def main():
    data = []

    print("Enter five values :")

    for i in range(5):
        no = int(input(f"Enter the number : "))
        data.append(no)

    print("Entered five elements are:")
    for value in data:
        print(value)

    MaxNumBet5(data)

if __name__ == "__main__":
    main()
