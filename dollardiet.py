class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def is_essential(self):
        essentials = ['food', 'transport', 'medicine', 'water']
        return self.category.lower() in essentials


class DollarDiet:
    def __init__(self, budget=1.0):
        self.budget = budget
        self.expenses = []

    def add_expense(self, name, amount, category):
        if amount <= 0:
            print("Amount must be greater than $0.")
            return
        expense = Expense(name, amount, category)
        self.expenses.append(expense)
        print(f"Added: {name} - ${amount:.2f} ({category})")

    def show_expenses(self):
        print("\n--- Expense Report ---")
        for i, exp in enumerate(self.expenses, 1):
            type_tag = "Essential" if exp.is_essential() else "Luxury"
            print(f"{i}. {exp.name} - ${exp.amount:.2f} [{exp.category}] ({type_tag})")
        print(f"\nTotal Spent: ${self.total_spent():.2f}")
        print(f"Remaining: ${self.budget - self.total_spent():.2f}")
        if self.total_spent() > self.budget:
            print("**Warning! You've exceeded your $1 budget!**")
        else:
            print("You're within the $1 challenge limit. Good job!")

    def total_spent(self):
        return sum(exp.amount for exp in self.expenses)


def run_dollardiet():
    print("Welcome to DollarDiet CLI - Your $1 Challenge Buddy!")
    app = DollarDiet()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. Show Expense Report")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Expense name: ")
            try:
                amount = float(input("Amount in $: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            category = input("Category (e.g. food, transport, luxury): ")
            app.add_expense(name, amount, category)

        elif choice == '2':
            app.show_expenses()

        elif choice == '3':
            print("Thanks for using DollarDiet CLI. Stay frugal!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    run_dollardiet()