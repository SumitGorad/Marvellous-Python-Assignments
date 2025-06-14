class Arithmatic:

    def __init__(self):       
        print("Inside constructor")
        self.Value1 = 0                 
        self.Value2= 0     

    def __del__(self):              
        print("Inside destructor")          

    def Accept(self):
        self.Value1 = int(input("Enter first value: "))
        self.Value2 = int(input("Enter second value: "))

    def Addition(self):
        result = self.Value1 + self.Value2
        return result

    def Subtraction(self):
        result = self.Value1 - self.Value2
        return result

    def Multiplication(self):        
        result = self.Value1 * self.Value2
        return result

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not allowed"
        if self.Value1 == 0:
            return "zero is not allowed"
        else:
            result = self.Value1 / self.Value2
        return result

def main():

    obj1 = Arithmatic()
    obj1.Accept()
    print("Addition of Value1 and Value2 is :", obj1.Addition())
    print("Subtraction of Value1 and Value2 is :", obj1.Subtraction())
    print("Multiplication of Value1 and Value2 is :", obj1.Multiplication())
    print("Division of Value1 and Value2 is :", obj1.Division())

    
    obj2 = Arithmatic()
    obj2.Accept()
    print("Addition of Value1 and Value2 is :", obj2.Addition())
    print("Subtraction of Value1 and Value2 is :", obj2.Subtraction())
    print("Multiplication of Value1 and Value2 is :", obj2.Multiplication())
    print("Division of Value1 and Value2 is :", obj2.Division())

    del Obj1
    del Obj2
    
if __name__ == "__main__":
    main()