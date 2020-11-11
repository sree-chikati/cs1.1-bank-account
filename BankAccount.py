from random import randint

class BankAccount:
    routing_number = 123456789
    #Step 3: Attributes:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = 0

    #Step 4: Methods:
    
    #Deposit Method
    def deposit(self, amount):
        """The deposit method will take one parameter amount 
        and will add amount to the balance. Also, it will print 
        the message: “Amount Deposited: $X.XX” """

        self.balance += amount
        print(f"Amount Deposited: ${amount}")
        

    #Witdraw Method
    def withdraw(self, amount):
        """ The withdraw method will take one parameter amount and
        will subtract amount from the balance. Also, it will print a 
        message, like “Amount Withdrawn: $X.XX”. If the user tries to
        withdraw an amount that is greater than the current balance, 
        print ”Insufficient funds.” and charge them with an overdraft
        fee of $10. """
        self.balance -= amount
        
        if amount > self.balance:
            print("Insufficient funds")
            self.balance -= 10

        else:
            print(f"Amount Withdrawn: ${amount}")
        
    
    #Get_Balance Method
    def get_balance(self):
        """ The get_balance method will print a user-friendly message with the account 
        balance and then also return the current balance of the account. """
        print(f"Your current balance is: ${self.balance}")
        return self.balance
        

    #Add_interest Method
    def add_interest(self):
        balance = self.balance
        """The add_interest method adds interest to the users balance. The annual interest 
        rate is 1% (i.e. 0.083% per month). Thus, the monthly interest is calculated by the
        following equation: interest = balance *  0.00083 """
        interest = balance *  0.00083
        self.balance += round(interest, 2)
        

    #Print_receipt Method
    def print_receipt(self):
        """ The print_receipt method prints a receipt with the account name, account number, and balance like this:
        Joi Anderson
        Account No.: ****5678
        Routing No.: 98765432
        Balance: $100.00   
        """
        account_num = str(self.account_number)

        print(f"Account Holder: {self.full_name}")
        print(f"Account number: ****{account_num[-4:]}")
        print(f"Routing number: {self.routing_number}")
        print(f"Balance: ${self.balance}")
        
    

#Step 5: Outside of the BankAccount class, define 3 different bank account examples using the BankAccount() object.
# Your examples should show you using the different methods above to demonstrate them working.

def createAccountNo():
    """8 digit account number generator"""
    account_no = ""
    for i in range(8):
        account_no += str(randint(0, 9))
    return int(account_no)


#Stretch Challange: Create a Bank Account
while True:
    print("Welcome to the BigHero ATM")
    atm_name = input("Which account would you like to check today? 1) Sree. 2) Hiro. 3) Baymax: ")
    atm_actions = input("Would you like to 1)Get Balance. 2)Deposit. 3) Withdraw: ")

    #Account 1
    if atm_name == str(1):
        Sree = BankAccount("Sree", createAccountNo(), 0)
        Sree.balance = 10
        if atm_actions == str(1):
            print("\n")
            print (Sree.get_balance())
            print("\n")
            print("This is your recepit: ")
            Sree.print_receipt()
            break
        
        elif atm_actions == str(2):
            print("\n")
            deposit = input("Enter the amount you would like to deposit: ")
            print (Sree.deposit(int(deposit)))
            print("\n")
            print("This is your recepit: ")
            Sree.print_receipt()
            break

        elif atm_actions == str(3):
            print("\n")
            withdraw = input("Enter the amount you would like to withdraw: ")
            print (Sree.withdraw(int(withdraw)))
            print("\n")
            print("This is your recepit: ")
            Sree.print_receipt()
            break

    #Account 2
    elif atm_name == str(2):
        Hiro = BankAccount("Hiro", createAccountNo(), 0)
        Hiro.balance = 100
        if atm_actions == str(1):
            print("\n")
            print (Hiro.get_balance())
            print("\n")
            print("This is your recepit: ")
            Hiro.print_receipt()
            break
        
        elif atm_actions == str(2):
            print("\n")
            deposit = input("Enter the amount you would like to deposit: ")
            print (Hiro.deposit(int(deposit)))
            print("\n")
            print("This is your recepit: ")
            Hiro.print_receipt()
            break

        elif atm_actions == str(3):
            print("\n")
            withdraw = input("Enter the amount you would like to withdraw: ")
            print (Hiro.withdraw(int(withdraw)))
            print("\n")
            print("This is your recepit: ")
            Hiro.print_receipt()
            break

    #Account 3
    elif atm_name == str(3):
        Baymax = BankAccount("Baymax", createAccountNo(), 0)
        Baymax.balance = 1000
        if atm_actions == str(1):
            print("\n")
            print (Baymax.get_balance())
            print("\n")
            print("This is your recepit: ")
            Baymax.print_receipt()
            break
        
        elif atm_actions == str(2):
            print("\n")
            deposit = input("Enter the amount you would like to deposit: ")
            print (Baymax.deposit(int(deposit)))
            print("\n")
            print("This is your recepit: ")
            Baymax.print_receipt()
            break

        elif atm_actions == str(3):
            print("\n")
            withdraw = input("Enter the amount you would like to withdraw: ")
            print (Baymax.withdraw(int(withdraw)))
            print("\n")
            print("This is your recepit: ")
            Baymax.print_receipt()
            break

    else: 
        print("Please select one of your accounts")


