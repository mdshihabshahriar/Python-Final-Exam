import random

class User:
    def __init__(self,name,email,address,account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = random.randint(10000,99999)
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0
        
    def deposit(self,amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount} TK")
        print(f"{amount} TK deposited successfully. Current balance: {self.balance} TK")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded!!!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount} TK")
            print(f"{amount} TK withdrawn successfully. Current balance: {self.balance} TK")
            
    def check_balance(self):
        print(f"Available balance: {self.balance} TK")
        return self.balance
    
    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
        
    def take_loan(self, amount):
        if self.loan_count >= 2:
            print("Loan limit reached!!!")
        else:
            self.balance += amount
            self.loan_count += 1
            self.transaction_history.append(f"Took loan: {amount} TK")
            print(f"Loan of {amount} TK approved. Current balance: {self.balance} TK")
            
    def transfer(self, amount, recipient):
        if amount > self.balance:
            print("Insufficient balance for transfer!!!")
        elif not isinstance(recipient, User):
            print("Account does not exist!!!")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred {amount} TK to {recipient.name}")
            recipient.transaction_history.append(f"Received {amount} TK from {self.name}")
            print(f"{amount} TK transferred to {recipient.name}. Your balance: {self.balance} TK")
            
class Admin:
    def __init__(self) -> None:
        self.users = {}
        self.total_balance = 0
        self.total_loan = 0
        self.loan_feature = True
        self.total_available_balance = 0
        self.count = 100
        
    def create_account(self,name, email, address, account_type):
        user = User(name,email,address,account_type)
        self.users[user.account_number] = user
        print(f"Account created for {name}. Account number: {user.account_number}")
        return user
    
    def delete_user_account(self, account_number):
        if account_number in self.users:
            del self.users[account_number]
            print(f"Account {account_number} deleted successfully.")
        else:
            print("Account not found")
            
    def view_user(self):
        print("All User Accounts:")
        for account_number, user in self.users.items():
            print(f"Account No: {account_number}, Name: {user.name}, Balance: {user.balance} TK")    
    
    def check_total_balance(self):
        self.total_balance = 0
        for user in self.users.values():
            self.total_balance += user.balance 
        return (self.total_balance)        
    
    def show_total_loan(self):  
        self.total_loan = 0
        for user in self.users.values():
            self.total_loan += user.balance
        return (self.total_loan)
    
    def available_balance(self):   
        self.total_available_balance = 0
        self.total_available_balance = self.get_total_balance() - self.show_total_loan()
        return self.total_available_balance
    
    def toggle_loan_feature(self,status):
        self.loan_feature = status
        if status:
            print("Loan feature is enabled.")
        else:
            print("Loan feature is disabled.")
            
admin = Admin()

while True:
    print("\n<----- Bank Management System ----->")
    print("1. Create User Account")
    print("2. User Login")
    print("3. Admin Login")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        # Create a new user account
        name = input("Enter name: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        account_type = input("Enter account type (Savings/Current): ")
        user = admin.create_account(name, email, address, account_type)

    elif choice == '2':
        # User Login
        account_number = int(input("Enter your account number: "))
        if account_number in admin.users:
            user = admin.users[account_number]
            while True:
                print("\n<--- User Menu --->")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. View Transaction History")
                print("5. Take Loan")
                print("6. Transfer Money")
                print("7. Logout")
                
                user_choice = input("Choose an option: ")
                
                if user_choice == '1':
                    amount = float(input("Enter amount to deposit: "))
                    user.deposit(amount)
                
                elif user_choice == '2':
                    amount = float(input("Enter amount to withdraw: "))
                    user.withdraw(amount)
                
                elif user_choice == '3':
                    user.check_balance()
                
                elif user_choice == '4':
                    user.view_transaction_history()
                
                elif user_choice == '5':
                    if admin.loan_feature:
                        amount = float(input("Enter loan amount: "))
                        user.take_loan(amount)
                    else:
                        print("Loan feature is currently disabled.")
                
                elif user_choice == '6':
                    recipient_account_number = int(input("Enter recipient's account number: "))
                    if recipient_account_number in admin.users:
                        recipient = admin.users[recipient_account_number]
                        amount = float(input("Enter amount to transfer: "))
                        user.transfer(amount, recipient)
                    else:
                        print("Recipient account does not exist.")
                
                elif user_choice == '7':
                    print("Logging out...")
                    break

                else:
                    print("Invalid option. Please try again.")
        else:
            print("Account not found.")

    elif choice == '3':
        # Admin Login
        while True:
            print("\n<--- Admin Menu --->")
            print("1. View All Accounts")
            print("2. Check Total Balance")
            print("3. Check Total Loan Amount")
            print("4. Toggle Loan Feature")
            print("5. Delete User Account")
            print("6. Logout")
            
            admin_choice = input("Choose an option: ")
            
            if admin_choice == '1':
                admin.view_user()
            
            elif admin_choice == '2':
                total_balance = admin.check_total_balance()
                print(f"Total available balance in the bank: {total_balance} TK")
            
            elif admin_choice == '3':
                total_loan = admin.show_total_loan()
                print(f"Total loan amount in the bank: {total_loan} TK")
            
            elif admin_choice == '4':
                status_input = input("Enter 1 to enable loan feature or 0 to disable: ")
                if status_input == '1':
                    admin.toggle_loan_feature(True)
                elif status_input == '0':
                    admin.toggle_loan_feature(False)
                else:
                    print("Invalid input. Please enter 1 or 0.")
            
            elif admin_choice == '5':
                account_number = int(input("Enter the account number to delete: "))
                admin.delete_user_account(account_number)
            
            elif admin_choice == '6':
                print("Logging out...")
                break
            
            else:
                print("Invalid option. Please try again.")

    elif choice == '4':
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please try again.")