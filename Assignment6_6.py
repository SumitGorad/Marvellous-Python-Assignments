def PrintStar(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end = " ")
        print() 
        
def main():
    print("Enter a number:")
    num = int(input())
    PrintStar(num)

if __name__ == "__main__":
    main()