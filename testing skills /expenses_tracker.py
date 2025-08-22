expenses = []

def new_expense(name, price):
    print('\n==============================')
    print('NEW ITEM:')
    print(f'Item added: Name: {name}, Price: £{price}')
    print('\n==============================')
    expenses.append(name)
    expenses.append(price)

def show_expenses():
    if not expenses:
        print('\nNo expenses\n')
        return
    total = 0
    print('\n==============================')
    print('ITEMS: ')
    for i in range(0, len(expenses), 2):
        name = expenses[i]
        price = expenses[i+1]
        print(f'Name: {name}, Price: £{price}\n')
        total += expenses[i+1]
    print(f'Total expense: £{total}')
        

    print('==============================')


def main():
    while True:
        print('\nExpenses tracker\n')
        print('Choose one of the following options:')
        print('1. Add expenses')
        print('2. Show expenses')
        print("3. Exit")
        choice = input(">> ")
        if choice == '1':
            try:
                name = input('Enter item name: ')
                price = float(input('Enter item price: '))
                new_expense(name, price)
            except:
                print('Invalid Input')
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            break 
        else:
            print('Invalid Input')       

if __name__ == "__main__":
    main()