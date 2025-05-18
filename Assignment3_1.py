def ListSum(list):
    total = 0
    for i in list:
        total = total + i
    print("Sum of all elements : ", total)

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

    ListSum(data)

if __name__ == "__main__":
    main()
