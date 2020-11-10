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
