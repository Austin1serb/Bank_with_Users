



class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, starting_balance=0): 
        
        self.balance = starting_balance
        self.int_rate = int_rate
        

        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount

        return self


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            
        else:
            print("You have insuffienct funds charging a $5 fee")
            self.balance -= 5 #late fee
            
        return self


    def display_account_info(self):
        print(f"Your account balance is: {self.balance}")

        return self


    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance -= interest

        return self
 

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.05,0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)		# we can call the BankAccount instance's methods

        return self
    
    def make_withdraw(self, amount):
            self.account.withdraw(amount)
    
            return self

    def display_user_info(self):
        self.account.display_account_info()


        return self
    

user1 = User("Austin", "Austin@gmail.com")
user1.make_deposit(50).make_withdraw(25).display_user_info()

# account1 = BankAccount(0.05, 50)
# account1.deposit(50).deposit(50).deposit(50).withdraw(75).yield_interest().display_account_info()

# account2 = BankAccount(0.05, 0).deposit(25).deposit(43).withdraw(2).withdraw(7).withdraw(5).withdraw(9).yield_interest().display_account_info


