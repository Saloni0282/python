import json

# Define user roles and their privileges
roles = {
    "admin": ["manage_snacks", "generate_sales_report"],
    "canteen_staff": ["manage_snacks"],
    "cashier": ["generate_sales_report"]
}

# Function to check user role and privileges
def check_role(username, privilege):
    if username in roles:
        return privilege in roles[username]
    return False

# Load snacks data from a JSON file
def load_snacks():
    try:
        with open("snacks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save snacks data to a JSON file
def save_snacks(snacks):
    with open("snacks.json", "w") as file:
        json.dump(snacks, file, indent=4)

# Load sales data from a JSON file
def load_sales():
    try:
        with open("sales.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save sales data to a JSON file
def save_sales(sales):
    with open("sales.json", "w") as file:
        json.dump(sales, file, indent=4)

# Main menu
def main_menu():
    print("Welcome to Mumbai Munchies Plus - Canteen Management System")
    print("1. Login")
    print("2. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        login()
    elif choice == '2':
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

# ... (previous code)

snacks = load_snacks()
sales = load_sales()

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Add authentication logic here (e.g., check against a user database)
    # For this exercise, assume hardcoded credentials.
    if username == 'admin' and password == 'password':
        admin_menu(username)
    elif username == 'canteen_staff' and password == 'password1':
        admin_menu(username)
    elif username == 'cashier' and password == 'password2':
        admin_menu(username)
    else:
        print("Invalid username or password. Please try again.")
        login()

#admin menu      
def admin_menu(username):
    print(f"Welcome, {username}!")
    print("1. Manage Snacks")
    print("2. Generate Sales Report")
    print("3. Logout")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        if check_role(username, "manage_snacks"):
            manage_snacks()
        else:
            print("You don't have permission to manage snacks.")
            admin_menu(username)
    elif choice == '2':
        if check_role(username, "generate_sales_report"):
            generate_sales_report()
        else:
            print("You don't have permission to generate sales reports.")
            admin_menu(username)
    elif choice == '3':
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        admin_menu(username)

# Function to manage snacks
def manage_snacks():
    while True:
        print("Manage Snacks:")
        print("1. View Snack Menu")
        print("2. Add New Snack")
        print("3. Update Snack Quantity")
        print("4. Remove Snack")
        print("5. Back to Admin Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_snacks()
        elif choice == '2':
            add_snack()
        elif choice == '3':
            update_snack_quantity()
        elif choice == '4':
            remove_snack()
        elif choice == '5':
            return  # Return to the admin menu
        else:
            print("Invalid choice. Please try again.")

# Function to add a new snack to the inventory
def add_snack():
    name = input("Enter the name of the new snack: ")
    category = input("Enter the category of the snack: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: $"))
    
    snack = {"name": name, "category": category, "quantity": quantity, "price": price}
    snacks.append(snack)
    save_snacks(snacks)
    print(f"{name} has been added to the inventory.")

# Function to update the quantity of an existing snack
def update_snack_quantity():
    display_snacks()
    index = int(input("Enter the number of the snack to update quantity: ")) - 1
    
    if 0 <= index < len(snacks):
        new_quantity = int(input("Enter the new quantity: "))
        snacks[index]["quantity"] = new_quantity
        save_snacks(snacks)
        print(f"Quantity for {snacks[index]['name']} has been updated to {new_quantity}.")
    else:
        print("Invalid snack number.")

# Function to remove a snack from the inventory
def remove_snack():
    display_snacks()
    index = int(input("Enter the number of the snack to remove: ")) - 1
    
    if 0 <= index < len(snacks):
        removed_snack = snacks.pop(index)
        save_snacks(snacks)
        print(f"{removed_snack['name']} has been removed from the inventory.")
    else:
        print("Invalid snack number.")

def display_snacks():
    print("Snack Menu:")
    for index, snack in enumerate(snacks, start=1):
        print(f"{index}. {snack['name']} ({snack['category']}): ${snack['price']} - Quantity: {snack['quantity']}")

# ... (previous code)

# Function to generate a basic sales report
def generate_sales_report():
    while True:
        print("Generate Sales Report:")
        print("1. View Sales Report")
        print("2. Add Sales Data")
        print("3. Back to Admin Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_sales_report()
        elif choice == '2':
            add_sales_data()
        elif choice == '3':
            break  # Return to the admin menu
        else:
            print("Invalid choice. Please try again.")

# Function to view the sales report
def view_sales_report():
    print("Sales Report:")
    total_sales = 0
    
    for snack in snacks:
        name = snack["name"]
        price = snack["price"]
        quantity_sold = snack.get("quantity_sold", 0)
        total_sales += snack.get("total_sales", 0)
        
        print(f"{name} - Quantity Sold: {quantity_sold}, Total Sales: ${total_sales:.2f}")
    
    print(f"Total Sales for All Snacks: ${total_sales:.2f}")

# Function to add sales data
def add_sales_data():
    print("Add Sales Data:")
    
    for index, snack in enumerate(snacks, start=1):
        name = snack["name"]
        quantity_sold = int(input(f"Enter the quantity of {name} sold: "))
        
        # Calculate the total sales for this snack
        sales = snack["price"] * quantity_sold
        snack["quantity_sold"] = quantity_sold
        snack["total_sales"] = sales
        save_snacks(snacks)
        
    print("Sales data has been recorded.")

if __name__ == "__main__":
    main_menu()
