import streamlit as st
import mysql.connector
import subprocess
import os
from PIL import Image
import bcrypt
import re

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amruta682@",
    database="milk_dairy_app"
)

# Hash a password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Function to insert a new user into the signup table
def insert_user(username, password):
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute("INSERT INTO signup (username, password) VALUES (%s, %s)", (username, hashed_password))
    conn.commit()
    cursor.close()


# Function to check if username and password exist in the signup table
def check_login(username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    if result:
        hashed_password = result[1]  # Assuming password is stored in the second column
        return validate_password(password, hashed_password)
    else:
        return False


# Validate a password


def validate_password(password):
    # Define a regular expression pattern for password validation
    # The pattern requires at least one uppercase letter, one lowercase letter,
    # one digit, one special character, and a minimum length of 8 characters
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    # Compile the regular expression pattern
    regex = re.compile(pattern)
    
    # Match the password against the pattern
    match = regex.match(password)
    
    # Return True if the password matches the pattern, otherwise False
    return bool(match)


def main():
    st.title("Login")
    current_dir = os.getcwd()

    img=Image.open("milk_dairy_image.jpg")
    st.image(
             img,
             #caption="Milk Dairy",
             width=700,
             channels="RGB"
        )
    img = Image.open("milk_dairy_image.jpg")
    

    # Login Section
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")


    if st.button("Login"):
        if check_login(username, password):
            # Open signup.py
            st.success("logged in successfull")
            subprocess.Popen(["streamlit", "run", "milk_dairy_app.py"])
            st.stop()
        else:
            st.error("new user")
            st.success("please SignUp!")
            # Open signup.py
            subprocess.Popen(["streamlit", "run", "signup.py"])
            st.stop()

if __name__ == "__main__":
    main()
