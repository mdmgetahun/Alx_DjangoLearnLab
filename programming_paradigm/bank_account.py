class BankAccount:
    def __init__(self, account_number, account_balance=0):
        self.account_number = account_number
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        return self.account_balance
    
def main():

    account = BankAccount("Amdetsion", 100)  
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
                print("Insufficient funds or wrong input.")
        elif choice == '3':
            print(f"Current Balance: ${account.display_balance()}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main() 
    
    
