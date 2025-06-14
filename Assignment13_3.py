import CheckPrime

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        return CheckPrime.ChkPrime(self.Value)

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    def Factors(self):
        print("Factors of given number are:")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

def main():

    obj1 = Numbers()
    obj1.Factors()
    print("Sum of factors is :", obj1.SumFactors())
    print("Is Prime :", obj1.ChkPrime())
    print("Is Perfect :", obj1.ChkPerfect())

    obj2 = Numbers()
    obj2.Factors()
    print("Sum of factors is :", obj2.SumFactors())
    print("Is Prime :", obj2.ChkPrime())
    print("Is Perfect :", obj2.ChkPerfect())

if __name__ == "__main__":
    main()
