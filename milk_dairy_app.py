import streamlit as st
import mysql.connector
from streamlit import session_state
from datetime import datetime, timedelta
import os
import re
import pandas as pd

# Define your username and password
USERNAME = "Amruta"
PASSWORD = "12345"


#Connect to MySQL database
conn = mysql.connector.connect(
     host="localhost",
     user="root",
     password="Amruta682@",
     database="milk_dairy_app"
 )
cursor = conn.cursor()
if conn.is_connected():
    print('connected successfull')
else:
    print("failed to connect")



# creating a new customer record
def create_customer():
    # Get the current working directory
    current_dir = os.getcwd()
    st.subheader("Create New Customer Record")
    customer_name = st.text_input("Enter Name")
    customer_address = st.text_input("Enter Address")
    customer_phone = st.text_input("Enter Phone Number")
    customer_password = st.text_input("Enter password")
    if st.button("Create Account"):
        phone_pattern = r"^\d{10}$"
        if not re.match(phone_pattern, customer_phone):
            st.error("Please enter a valid 10-digit phone number.")
        else:
            cursor.execute("INSERT INTO customer (customer_name, customer_address, customer_phone,customer_password) VALUES (%s, %s, %s, %s)", (customer_name, customer_address,customer_phone,customer_password))
            conn.commit()
            st.success("Customer account created successfully!")



# displaying customer records
def display_customers():
    st.subheader("Customer Records")
    cursor.execute("SELECT customer_id, customer_name, customer_address, REPLACE(customer_phone, ',', '') FROM customer")
    customers = cursor.fetchall()
    # Add a serial number column to the data
    customers_with_serial = [(i, *customer) for i, customer in enumerate(customers, start=1)]
    df = pd.DataFrame(customers_with_serial, columns=[ "Serial No", "Customer ID", "Customer Name", "Customer Address", "Customer Phone"])
    st.write(df)


# creating a new owner record
def create_owner():
    st.subheader("Create New Owner Record")
    owner_name = st.text_input("Enter Name")
    owner_address = st.text_input("Enter Address")
    owner_phone = st.text_input("Enter  Phone Number")
    owner_password = st.text_input("Enter password")
    if st.button("Create Account"):
        phone_pattern = r"^\d{10}$"
        if not re.match(phone_pattern, owner_phone):
            st.error("Please enter a valid 10-digit phone number.")
        else:
            cursor.execute("INSERT INTO owner (owner_name, owner_address, owner_phone,owner_password) VALUES (%s, %s, %s, %s)", (owner_name, owner_address, owner_phone, owner_password))
            conn.commit()
            st.success("Owner account created successfully!")



# displaying owner records
def display_owners():
    st.subheader("Owner Records")
    cursor.execute("SELECT owner_id, owner_name, owner_address, REPLACE(owner_phone, ',', '') FROM owner")
    owners = cursor.fetchall()
    owners_with_serial = [(i, *owner) for i, owner in enumerate(owners, start=1)]
    df = pd.DataFrame(owners_with_serial, columns=[ "Serial No", "Owner ID", "Owner Name", "Owner Address", "Owner Phone"])
    st.write(df)



# milk detail records
def milk_detail():
    st.subheader("Manage Milk Detail Records")
    # Dictionary mapping milk types to default prices per unit
    default_prices = {'Cow Milk': 25, 'Buffalo Milk': 60, 'Goat Milk': 45, 'Sheep Milk': 50}    
    # Set the default milk type
    default_milk_type = 'Cow Milk'
    milk_types = ('Cow Milk', 'Buffalo Milk', 'Goat Milk', 'Sheep Milk')    
    # Default price per unit for 'Cow Milk'
    default_price_per_unit = default_prices[default_milk_type]    
    # Default index for 'Cow Milk'
    milk_type_index = 0  
    # Selectbox for milk types
    milk_type = st.selectbox('Select the type of Milk', milk_types, index=milk_type_index, format_func=lambda x: default_milk_type if x == '' else x)    
    # Set default price per unit based on selected milk type
    default_price_per_unit = default_prices[milk_type]    
    # Input field for price per unit
    price_per_unit = st.number_input("Enter Milk Price", value=default_price_per_unit, min_value=10, step=5)    
    date_of_packaging = st.date_input("Enter the Date of packaging")
    # Calculate date of expiry based on date of manufacture + 3 days
    date_of_expiry = date_of_packaging + timedelta(days=3)
    # Display the calculated date of expiry
    st.write(f"Date of Expiry: {date_of_expiry.strftime('%Y-%m-%d')}")    
    if st.button("Save Details"):
    # Insert data into the database
        cursor.execute("INSERT INTO milk_detail (milk_type, price_per_unit, date_of_packaging) VALUES (%s, %s, %s)", (milk_type, float(price_per_unit), str(date_of_packaging)))
        conn.commit()
        st.success("Milk Details Saved successfully!")
    




# Function to fetch owner details from the database
def get_owner_details():
    cursor.execute("SELECT owner_id, owner_name, owner_address, owner_phone FROM owner")
    owner_details = cursor.fetchall()
    return owner_details
# Function to format owner details for display
def format_owner_details(owner_details):
    formatted_details = []
    for owner in owner_details:
        formatted_details.append(f"{owner[1]} - ID: {owner[0]}, Address: {owner[2]}, Phone: {owner[3]}")
    return formatted_details
# function to get the price per unit from database
def get_price_per_unit(cursor, milk_type):
    cursor.execute("SELECT price_per_unit FROM milk_detail WHERE milk_type = %s", (milk_type,))
    result = cursor.fetchone()
    if result:
        return result[0] 
    else:
        return None




# displaying order details
def order_detail():
    st.subheader("ORDER DETAIL")
    # Owner Information
    st.subheader("Owner Information")    
    # Fetch owner details from the database
    owner_details = get_owner_details()
    formatted_owner_details = format_owner_details(owner_details)    
    # Populate dropdown with formatted owner details
    owner_selection = st.selectbox("Select Owner:", formatted_owner_details)
    # Extract owner name, ID, and address from the selected value
    owner_name = owner_selection.split(" - ")[0]
    owner_id = owner_selection.split(" - ID: ")[1].split(", Address: ")[0]
    owner_address = owner_selection.split(", Address: ")[1].split(", Phone: ")[0]
    owner_phone = owner_selection.split(", Phone: ")[1]
    
    # Milk Detail
    st.subheader("Milk Detail")
    milk_type = st.selectbox('Select the type of Milk', ('Cow Milk', 'Buffalo Milk', 'Goat Milk', 'Sheep Milk'))
    # Retrieve the price per unit for the selected milk type from the database
    price_per_unit = get_price_per_unit(cursor, milk_type)
    # Display the retrieved price per unit
    if price_per_unit is not None:
        st.write(f"Price per Unit for {milk_type}: {price_per_unit}")
    else:
        st.write(f"Price per Unit for {milk_type} not found in the database")
    quantity_bought = st.number_input("Quantity Purchased in Litres:", min_value=0, step=1)
    # price_per_unit = st.number_input("Price per Unit:", value=frozen_price_per_unit, min_value=0, step=1)
    total_cost = quantity_bought * price_per_unit
    st.write(f"Total Cost: {total_cost}")
    # Save button
    if st.button("Place Order"):
        # Insert the transaction details into the database
        cursor.execute("INSERT INTO order_detail (owner_name, owner_id, owner_address, owner_phone, milk_type, quantity_bought, price_per_unit, total_cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (owner_name, owner_id, owner_address, owner_phone, milk_type, quantity_bought, price_per_unit, total_cost))
        conn.commit()
        order_id = cursor.lastrowid  
        st.success(f"Order Placed successfully! Order ID: {order_id}")
        
        


# Function to generate bill for a given order_id
def generate_bill(order_id):
    # Retrieve order details along with bill_id from the database based on order_id
    cursor.execute("SELECT owner_name, owner_id, milk_type, quantity_bought, price_per_unit FROM order_detail  WHERE order_id = %s", (order_id,))
    order_details = cursor.fetchone()
    if order_details:
        owner_name, owner_id, milk_type, quantity_bought, price_per_unit = order_details
        total_cost = quantity_bought * price_per_unit
        cursor.execute("INSERT INTO generate_bill (owner_name, owner_id, milk_type, quantity_bought, price_per_unit, total_cost) VALUES (%s, %s, %s, %s, %s, %s)", (owner_name, owner_id, milk_type, quantity_bought, price_per_unit, total_cost))
        conn.commit()
        # Get the auto-generated bill_id
        bill_id = cursor.lastrowid
        # Include bill_id in the displayed bill
        bill = f"========== Bill ==========\n"
        bill += f"Bill ID: {bill_id}\n"
        bill += f"Order ID: {order_id}\n"
        bill += f"Owner Name: {owner_name}\n"
        bill += f"Owner ID: {owner_id}\n"
        bill += f"Milk Type: {milk_type}\n"
        bill += f"Quantity Bought in Litres: {quantity_bought}\n"
        bill += f"Price per Unit: {price_per_unit}\n"
        bill += f"Total Cost: {total_cost}\n"       
        return bill
    else:
        return None
             


# def get_total_cost_for_bill_id(bill_id,conn):
#     try:
#         if conn.is_connected():
#             cursor = conn.cursor()
#             # Execute SQL query to fetch total cost for the provided bill ID
#             cursor.execute("SELECT total_cost FROM generate_bill WHERE bill_id = %s", (bill_id,))
#             total_cost = cursor.fetchone()[0]  # Fetch the total cost from the result
#      # Close the database connection
#             cursor.close()
#             return total_cost
#         else:
#             print("MySQL Connection is not available.")
#             return None
#     except mysql.connector.Error as e:
#         print("Error fetching total cost:", e)
#         return None

# # Function to retrieve all bill IDs for a specific owner ID
# def get_bills_for_owner(owner_id):
#     cursor.execute("SELECT bill_id FROM generate_bill WHERE owner_id = %s", (owner_id,))
#     bill_ids = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return [str(bill_id[0]) for bill_id in bill_ids]  # Convert to string for display in selectbox
# # Function to insert payment details into the database
# def insert_payment_details(bill_id, transaction_datetime, total_amount_paid, outstanding_due, transaction_mode):
#     cursor.execute("INSERT INTO payment_details (bill_id, transaction_datetime, total_amount_paid, outstanding_due, transaction_mode) VALUES (%s, %s, %s, %s, %s)",
#                    (bill_id, transaction_datetime, total_amount_paid, outstanding_due, transaction_mode))
#     conn.commit()
#     cursor.close()
#     conn.close()
# # Function to retrieve payment details from the database
# def get_payment_details():
#     cursor.execute("SELECT * FROM payment_details")
#     payment_details = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return payment_details
# # Function to retrieve the total cost associated with a bill ID from the milk_details table
# def get_total_cost_for_bill_id(bill_id, conn):
#     try:
#         if conn.is_connected():
#             cursor = conn.cursor()
#             cursor.execute("SELECT total_cost FROM milk_details WHERE bill_id = %s", (bill_id,))
#             total_cost = cursor.fetchone()[0]
#             if total_cost:
#                 # Close the cursor
#                 cursor.close()
#                 return total_cost[0]  # Return the total cost if found
#             else:
#                 print("Total cost not found for bill ID:", bill_id)
#                 return None
#         else:
#             print("MySQL Connection is not available.")
#             return None            
#     except mysql.connector.Error as e:
#         print("Error fetching total cost:", e)
#         return None


def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    if st.sidebar.button("Login"):
        if username == USERNAME and password == PASSWORD:
            session_state.logged_in = True
        else:
            st.error("Invalid username or password. Please try again.")

# Function to display the main menu
def main_menu():
    # Main Menu
    menu = ["Create Customer", "Display Customers", "Create Owner", "Display Owners", "Milk Detail", "Order Details", "Generate Bill"]
    choice = st.sidebar.selectbox("Menu", menu)



def main():
    st.title("Milk Dairy Management System")
    # Navigation

    menu = ["Create Customer", "Display Customers", "Create Owner", "Display Owners", "Milk Detail", "Order Details", "Generate Bill"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Create Customer":
        create_customer()
    elif choice == "Display Customers":
        display_customers()
    elif choice == "Create Owner":
        create_owner()
    elif choice == "Display Owners":
        display_owners()
    elif choice == "Milk Detail":
        milk_detail()
    elif choice == "Order Details":
        order_detail()
    elif choice == "Generate Bill":
        order_id = st.text_input("Enter Order ID:")
        if st.button("Generate Bill"):
            generated_bill = generate_bill(order_id)
            if generated_bill:
                with st.expander("Generated Bill"):
                    st.text(generated_bill)
                    # st.success(f"Bill Generated Successfull! Bill ID: {bill_id}")
            else:
                st.error("Failed to generate bill. Order ID not found.")
    # elif choice == "Payment Details":
    #     st.title("Payment Details ")

    #     cursor = conn.cursor()

    #     cursor.execute("SELECT DISTINCT owner_id FROM generate_bill")
    #     owner_ids = cursor.fetchall()

    #     # Input field for selecting owner ID
    #     owner_id = st.selectbox("Select Owner ID:", [str(owner_id[0]) for owner_id in owner_ids])

    #     # Fetch all bill IDs for the selected owner ID
    #     bill_ids = get_bills_for_owner(owner_id)

    #     # Input field for selecting bill ID
    #     bill_id = st.selectbox("Select Bill ID:", bill_ids)
    #     total_cost = get_total_cost_for_bill_id(bill_id, conn)
    #     if total_cost is not None:
    #         st.write(f"Total Cost: {total_cost}")
    #     # Input fields for entering payment details
    #     transaction_datetime = st.date_input(" Transaction Date:")
    #     transaction_time = st.time_input("Transaction Time:")
    #     total_amount_paid = st.number_input("Total Amount Paid:", min_value=0.00)
    #     outstanding_due = st.number_input(" Outstanding Due:", min_value=0.00)
    #     transaction_mode = st.selectbox("Transaction Mode:", ["Cash", "Credit Card", "Bank Transfer", "Other"])

    #     # Combine date and time inputs into a single datetime object
    #     transaction_datetime = datetime.combine(transaction_datetime, transaction_time)

    #     # Button to insert payment details into the database
    #     if st.button("Insert Payment Details"):
    #         insert_payment_details(bill_id, transaction_datetime, total_amount_paid, outstanding_due, transaction_mode)
    #         st.success("Payment details inserted successfully.")

    #     # Button to fetch and display payment details
    #     if st.button("Fetch Payment Details"):
    #         payment_details = get_payment_details()
    #         if not payment_details:
    #             st.error("No payment details found in the database.")
    #         else:
    #             st.subheader("Payment Details")
    #             st.write(payment_details)

        # Close cursor and connection
        # conn.close()
        # cursor.close()


if __name__ == "__main__":
    main()

