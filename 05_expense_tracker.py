# Expense Tracker

list_expenses = []

def add_expense():
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return
    
    category = input("Enter the category to put the expense in: ").strip()
    note = input("Enter any additional note: ").strip()
    
    entry = {"amount": amount, "category": category, "note": note}
    list_expenses.append(entry)
    print("✅ Expense added successfully!")

def view_expenses():
    if not list_expenses:
        print("No expense yet.")
        return
    
    for i, exp in enumerate(list_expenses, start=1):
        print(f"{i}. Amount: {exp.get('amount', 0)}, "
              f"Category: {exp.get('category', 'N/A')}, "
              f"Note: {exp.get('note', '')}")

def total_exp():
    total = sum(exp.get("amount", 0) for exp in list_expenses)
    print(f"💰 Total expenses: {total}")

def cat_exp():
    category = input("Enter the category (or T to view all): ").strip()
    if category.lower() == "t":
        view_expenses()
    else:
        filtered = [exp["amount"] for exp in list_expenses if exp["category"].lower() == category.lower()]
        if filtered:
            print(f"Total expenses in '{category}': {sum(filtered)}")
        else:
            print(f"No expenses found in category '{category}'.")

# Main Loop
while True:
    print("\n__Expense Tracker__")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. View total expenditure")
    print("4. View expenses categorically")
    print("5. Quit")
    
    menu_choice = input("Please enter your choice: ").strip()
    
    if menu_choice == "1":
        add_expense()
    elif menu_choice == "2":
        view_expenses()
    elif menu_choice == "3":
        total_exp()
    elif menu_choice == "4":
        cat_exp()
    elif menu_choice == "5":
        print("Thanks, have a great day ❤️")
        break
    else:
        print("Invalid choice T_T")
