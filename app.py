import streamlit as st
import pandas as pd
import os

st.title("Organization Registration Form")

# Form inputs
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
department = st.selectbox(
    "Department",
    ["HR", "IT", "Finance", "Marketing", "Operations"]
)
password = st.text_input("Password", type="password")

submit = st.button("Register")

# File to store data
file = "users.csv"

if submit:
    if name and email and phone and password:
        
        new_user = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Department": department,
            "Password": password
        }

        if os.path.exists(file):
            df = pd.read_csv(file)
            df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
        else:
            df = pd.DataFrame([new_user])

        df.to_csv(file, index=False)

        st.success("Registration Successful!")

    else:
        st.error("Please fill all fields")