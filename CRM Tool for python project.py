import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('crm.db')
cursor = conn.cursor()

# Create a table for storing customer information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        address TEXT
    )
''')
conn.commit()

# Function to add a new customer
def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone number: ")
    address = input("Enter customer address: ")

    try:
        cursor.execute('''
            INSERT INTO customers (name, email, phone, address)
            VALUES (?, ?, ?, ?)
        ''', (name, email, phone, address))
        conn.commit()
        print("Customer added successfully!")
    except sqlite3.IntegrityError:
        print("Error: A customer with this email already exists.")

# Function to view all customers
def view_customers():
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    if customers:
        for customer in customers:
            print(customer)
    else:
        print("No customers found.")

# Function to update a customer's information
def update_customer():
    customer_id = input("Enter the ID of the customer to update: ")
    field = input("Which field do you want to update? (name/email/phone/address): ").lower()
    new_value = input(f"Enter new value for {field}: ")

    if field in ["name", "email", "phone", "address"]:
        cursor.execute(f"UPDATE customers SET {field} = ? WHERE id = ?", (new_value, customer_id))
        conn.commit()
        print("Customer information updated successfully!")
    else:
        print("Invalid field selection.")

# Function to delete a customer
def delete_customer():
    customer_id = input("Enter the ID of the customer to delete: ")
    cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    conn.commit()
    print("Customer deleted successfully!")

# Function to search for a customer by email
def search_customer():
    email = input("Enter the email of the customer to search: ")
    cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
    customer = cursor.fetchone()
    if customer:
        print("Customer found:", customer)
    else:
        print("No customer found with that email.")

# Main program loop
def main():
    while True:
        print("\nCustomer Relationship Management Tool")
        print("1. Add Customer")
        print("2. View All Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Search Customer")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            add_customer()
        elif choice == '2':
            view_customers()
        elif choice == '3':
            update_customer()
        elif choice == '4':
            delete_customer()
        elif choice == '5':
            search_customer()
        elif choice == '6':
            print("Exiting CRM tool.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the CRM program
if __name__ == "__main__":
    main()

# Close the connection when done
conn.close()
