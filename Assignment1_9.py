def EvenNum(no):
                count , i = 0,2
                while (count < no):
                        print(i ,end=" ")
                        i = i + 2
                        count = count + 1

number = int(input("Enter a number : "))
even = EvenNum(number)
