def FrequencyOfNum(l):
    num = int(input("Enter the number to find its frequency : "))
    count = 0
    for i in l:
        if i == num:
            count = count + 1

    print("Frequency of entered number from the list is : ", count)

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

    FrequencyOfNum(data)

if __name__ == "__main__":
    main()
