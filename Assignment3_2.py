def MaxNum(l):
    maxn = l[0]
    for i in range(1,len(l)):
        if l[i] > maxn:
            maxn = l[i]

    print("Maximum number from the list is : ", maxn)

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

    MaxNum(data)

if __name__ == "__main__":
    main()
