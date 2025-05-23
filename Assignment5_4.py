def MaxNumBet3(l):
    a = l[0]
    b = l[1]
    c = l[2]

    if b <= a >= c:
        maxnum = a
    elif a <= b >= c:
        maxnum = b
    else:
        maxnum = c

    print("Largest number is : ", maxnum)

def main():
    data = []

    print("Enter three values :")

    for i in range(3):
        no = int(input(f"Enter three number : "))
        data.append(no)

    print("Entered elements are:")
    for value in data:
        print(value)

    MaxNumBet3(data)

if __name__ == "__main__":
    main()
