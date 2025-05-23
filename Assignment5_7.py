def AreaOfRect(l,w):
    area = l * w
    return area

def PerimeterOfRect(l,w):
    perimeter = ((2 * l) + (2 * w))
    return perimeter

def main():
    length = int(input("Enter the length : "))
    width = int(input("Enter the width : ")) 

    A = AreaOfRect(length,width)
    print("Area of rectangle is : " , A)

    B = PerimeterOfRect(length,width)
    print("Perimeter of rectangle is : " , B)

if __name__ == "__main__":
    main()