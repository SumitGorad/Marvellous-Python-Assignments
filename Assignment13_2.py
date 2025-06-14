class BankAccount:

    ROI = 10.5  

    def __init__(self):

        self.Name = input("Enter Account Holder Name : ")
        self.Amount = int(input("Enter Initial Amount : "))

    def Deposit(self):

        deposit_amount = int(input("Enter amount to deposit : "))
        self.Amount = self.Amount + deposit_amount
        print("The New Balance is : Rs.",self.Amount)

    def Withdraw(self):

        withdraw_amount = int(input("Enter amount to withdraw : "))
        if withdraw_amount <= self.Amount:
            self.Amount = self.Amount - withdraw_amount
            print("The New Balance is :Rs.",self.Amount)
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"ROI is :Rs.",interest)

    def Display(self):
        print("Account Holder name is : ",self.Name)
        print("Account Balance is : ",self.Amount)


# Main Function
def main():

    acc1 = BankAccount()
    acc1.Display()
    acc1.Deposit()
    acc1.Withdraw()
    acc1.CalculateInterest()
    acc1.Display()

    acc2 = BankAccount()
    acc2.Display()
    acc2.Deposit()
    acc2.Withdraw()
    acc2.CalculateInterest()
    acc2.Display()

if __name__ == "__main__":
    main()
