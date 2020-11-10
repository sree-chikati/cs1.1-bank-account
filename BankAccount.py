from random
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
        account_no = str(self.account_number)

        print(f"Account Holder: {self.full_name}")
        print(f"Account number: ****{account_no[-4:]}")
        print(f"Routing number: {self.routing_number}")
        print(f"Balance: ${self.balance}")
    



