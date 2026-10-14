def add_expense(expenses, amount, category):
    # Add a new expense as a dict to the expenses list
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    # Iterate over each expense dict and display its fields
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    # map() extracts the 'amount' from each expense dict
    # sum() adds all amounts together
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    # filter() keeps only expenses where category matches
    # Returns a filter iterator — consumed by print_expenses()
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = []   # in-memory list — resets every time the program runs

    while True:     # loop until user chooses to exit
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))      # float for decimals
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            # filter returns an iterator — passed directly to print_expenses
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break   # exits the while True loop

main()