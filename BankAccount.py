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
    