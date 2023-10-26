'''
BankAccount.py program
which bank is best

code a program that helps users decide which bank is the best for them to invest with.

this program allows users to input their name, initial deposit, and investment length, and then see what their final balance would be for each bank.
'''


class BankAccount:
    def __init__(self, owner, initial_deposit, length_of_investment):
        self.owner = owner
        self.balance = initial_deposit
        self.length_of_investment = length_of_investment


class Bank:
    def __init__(self, name, base_interest_rate, interest_increase_rate, increase_interval):
        self.name = name
        self.base_interest_rate = base_interest_rate
        self.interest_increase_rate = interest_increase_rate
        self.increase_interval = increase_interval

    def calculate_final_balance(self, account):
        years = account.length_of_investment
        total_interest = 0

        for year in range(years):
            if (year + 1) % self.increase_interval == 0:
                self.base_interest_rate += self.interest_increase_rate
            interest = account.balance * self.base_interest_rate
            account.balance += interest
            total_interest += interest

        return account.balance, total_interest


# Create bank objects with their specific attributes
bank_of_america = Bank("Bank of America", 0.005, 0.001, 5)
chase = Bank("Chase", 0.004, 0.002, 10)
wells_fargo = Bank("Wells Fargo", 0.003, 0.003, 15)

while True:
    owner = input("Enter your name (or 'quit' to exit): ")
    if owner.lower() == 'quit':
        break

    initial_deposit = float(input("Enter your initial deposit: $"))
    length_of_investment = int(
        input("Enter the length of investment in years: "))

    account = BankAccount(owner, initial_deposit, length_of_investment)

    print("Choose a bank:")
    print("1. Bank of America")
    print("2. Chase")
    print("3. Wells Fargo")

    bank_choice = int(input("Enter the number of the selected bank: "))

    if bank_choice == 1:
        final_balance, total_interest = bank_of_america.calculate_final_balance(
            account)
    elif bank_choice == 2:
        final_balance, total_interest = chase.calculate_final_balance(account)
    elif bank_choice == 3:
        final_balance, total_interest = wells_fargo.calculate_final_balance(
            account)
    else:
        print("Invalid choice. Please select a valid bank.")
        continue

    print(
        f"Final balance for {owner} after {length_of_investment} years in {bank_of_america.name}: ${final_balance:.2f}")
    print(f"Total interest earned: ${total_interest:.2f}")
