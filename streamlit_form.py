import streamlit as st

st.set_page_config(page_title="Hlasela Mafuta Registration", layout="centered")
st.markdown("## 📋 Hlasela Mafuta Registration Form")
st.markdown("Please fill in your details below:")

id_number = st.text_input("1. ID Number")
acc_number = st.text_input("2. Account Number")
dob = st.date_input("3. Date of Birth")

if st.button("Finish"):
    if id_number and acc_number and dob:
        st.success(f"✅ Submission recorded!\n\nID: {id_number}\nAccount: {acc_number}\nDOB: {dob}")
    else:
        st.error("❌ Please fill in all fields.")
