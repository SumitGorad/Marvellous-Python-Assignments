def Table(n):
    for i in range(1, 11):
        print(n, "*", i, "=", n * i)
            
def main():
    print("Enter a number :")
    num = int(input())

    Table(num)

if __name__ == "__main__":
    main()