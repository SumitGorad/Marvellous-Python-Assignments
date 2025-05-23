def SumOfEven(l):
    ans = 0
    for i in l:
        ans = ans + i
    print("Sum of even numbers from 1 to 100 is : ", ans)

def PrintNum(n):
    data = []
    for no in range(1, n):
        if no % 2 == 0:
            data.append(no)
    SumOfEven(data)

def main():
    PrintNum(101)

if __name__ == "__main__":
    main()
