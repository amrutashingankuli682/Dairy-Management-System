import streamlit as st
import mysql.connector
import subprocess
from PIL import Image
import bcrypt
# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amruta682@",
    database="milk_dairy_app"
)

def check_login(username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    return result is not None

# Hash a password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Validate a password
def validate_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Function to insert new username and password into the login table
def insert_login(username, password):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()

def main():
    st.title("Sign Up")
    img=Image.open("milk_dairy_image2.jpg")
    st.image(
             img,
             #caption="Milk Dairy",
             width=700,
             channels="RGB"
        )
    img = Image.open("milk_dairy_image2.jpg")
    # Signup Section
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if check_login(username, password):
            st.success("sign up Successful!")
            # Open signup.py
            subprocess.Popen(["streamlit", "run", "milk_dairy_app.py"])
            st.stop()
        else:
            st.error("new user")
            insert_login(username, password)
            st.success("Sign up Successful!")
            # Open signup.py
            subprocess.Popen(["streamlit", "run", "milk_dairy_app.py"])
            st.stop()


if __name__ == "__main__":
    main()
