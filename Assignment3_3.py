def MinNum(l):
    minnum = l[0]
    for i in range(1,len(l)):
        if l[i] < minnum:
            minnum = l[i]

    print("Minimum number from the list is : ", minnum)

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

    MinNum(data)

if __name__ == "__main__":
    main()
