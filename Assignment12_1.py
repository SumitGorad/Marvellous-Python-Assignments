class Demo:
    Value = "Marvellous"        

    def __init__(self, A, B):        
        print("Inside constructor")
        self.no1 = A                  
        self.no2 = B                

    def __del__(self):              
        print("Inside destructor")

    def Fun(self):             
        print("Inside Instance method Fun")
        print("Emplyee Name : ",self.no1)
        print("Emplyee Salary : ",self.no2)

    def Gun(self):              
        print("Inside Instance method Gun")
        print("Emplyee Name : ",self.no1)
        print("Emplyee Salary : ",self.no2)   
        
def main():

    Obj1 = Demo(11,21)     
    Obj2  = Demo(51,101)     

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

    del Obj1
    del Obj2
    
if __name__ == "__main__":
    main()