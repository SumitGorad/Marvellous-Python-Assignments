def ChkNum(no):
    if(no > 0):
          print("Positive Number")
    elif(no < 0):
          print("Negative Number")
    else:
          print("Zero")

number = int(input("Enter a number : "))
ChkNum(number)