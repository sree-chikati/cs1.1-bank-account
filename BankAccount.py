from random import randint
class BankAccount:
    #Step 3: Attributes:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = 0

    #Step 4: Methods:
    
    #Deposit Method
    def deposit(self, amount):
        """The deposit method will take one parameter amount 
        and will add amount to the balance. Also, it will print 
        the message: “Amount Deposited: $X.XX” """

        self.balance += amount
        print(f"Amount Deposited: ${amount}")
        print("\n")

    #Witdraw Method
    def withdraw(self, amount):
        """ The withdraw method will take one parameter amount and
        will subtract amount from the balance. Also, it will print a 
        message, like “Amount Withdrawn: $X.XX”. If the user tries to
        withdraw an amount that is greater than the current balance, 
        print ”Insufficient funds.” and charge them with an overdraft
        fee of $10. """

        if amount > self.balance:
            print("Insufficient funds")
            self.balance -=10

        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")
        print("\n")
    
    #Get_Balance Method
    def get_balance(self):
        """ The get_balance method will print a user-friendly message with the account 
        balance and then also return the current balance of the account. """
        print(f"Your current balance is: ${self.balance}")
        return self.balance
        print("\n")

    #Add_interest Method
    def add_interest(self):
        balance = self.balance
        """The add_interest method adds interest to the users balance. The annual interest 
        rate is 1% (i.e. 0.083% per month). Thus, the monthly interest is calculated by the
        following equation: interest = balance *  0.00083 """
        interest = balance *  0.00083
        self.balance += round(interest, 2)
        print("\n")

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
        print("\n")
    

#Step 5: Outside of the BankAccount class, define 3 different bank account examples using the BankAccount() object.
# Your examples should show you using the different methods above to demonstrate them working.

def createAccountNo():
    """8 digit account number generator"""
    account_no = ""
    for i in range(8):
        account_no += str(randint(0, 9))
    return int(account_no)

# Account 1
Sree = BankAccount("Sree", createAccountNo(), 123456789, 0)
Sree.balance = 10
Sree.withdraw(5)
Sree.deposit(10)
Sree.print_receipt()

# Account 2
Hiro = BankAccount("Hiro", createAccountNo(), 123456789, 0)
Hiro.balance = 100
Hiro.withdraw(50)
Hiro.deposit(15)
Hiro.print_receipt()

# Account 3 
Baymax = BankAccount("Baymax", createAccountNo(), 123456789, 0)
Baymax.balance = 1000
Baymax.withdraw(500)
Baymax.deposit(25)
Baymax.print_receipt()





