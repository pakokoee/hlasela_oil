import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Hlasela Mafuta Registration", layout="centered")
st.markdown("## 📋 Hlasela Mafuta Registration Form")
st.markdown("Please fill in your details below:")

# Define input fields BEFORE using them
id_number = st.text_input("1. ID Number")
acc_number = st.text_input("2. Account Number")
dob = st.date_input("3. Date of Birth")

# Button logic AFTER inputs are defined
if st.button("Finish"):
    if id_number and acc_number and dob:
        new_data = pd.DataFrame([[id_number, acc_number, str(dob)]],
                                columns=["ID Number", "Account Number", "Date of Birth"])
        
        # Save to CSV
        if os.path.exists("responses.csv"):
            existing = pd.read_csv("responses.csv")
            updated = pd.concat([existing, new_data], ignore_index=True)
        else:
            updated = new_data

        updated.to_csv("responses.csv", index=False)
        st.success("✅ Submission recorded successfully!")
    else:
        st.error("❌ Please fill in all fields.")



