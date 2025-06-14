class Circle:
    PI = 3.14         

    def __init__(self,):   
        print("Inside constructor")
        self.Radius = 0.0                  
        self.Area = 0.0               
        self.Circumference = 0.0  

    def __del__(self):              
        print("Inside destructor")               

    def Accept(self):              
        print("Inside Instance method Accept")
        self.Radius = int(input("Enter The Radius: "))

        
    def CalculateArea(self): 
        print("Inside Instance method CalculateArea")
        self.Area = Circle.PI * self.Radius * self.Radius


    def CalculateCircumference(self):
        print("Inside Instance method CalculateCircumference")
        self.Circumference = 2 * Circle.PI * self.Radius

 
    def Display(self):
        print("Inside Instance method Display")
        print("Radius of a circle is : ",self.Radius)
        print("Area of a circle is : ",self.Area)
        print("Circumference of a circle is : ",self.Circumference)

def main():

    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    
    obj2 = Circle()
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

    del Obj1
    del Obj2
    
if __name__ == "__main__":
    main()