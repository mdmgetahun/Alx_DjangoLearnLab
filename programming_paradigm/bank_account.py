class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount is not None and amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
    
def main(account):

    account = BankAccount(100)  
    while True:

        print("Choose Action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            if account.deposit(amount):
                print(f"Deposited: ${amount}")
            else:
                print("Wrong Input")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insuffaicient funds.")
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main(account=BankAccount(100)) 
    
