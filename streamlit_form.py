import pandas as pd
import os

# When user clicks "Finish"
if st.button("Finish"):
    if id_number and acc_number and dob:
        new_data = pd.DataFrame([[id_number, acc_number, str(dob)]],
                                columns=["ID Number", "Account Number", "Date of Birth"])
        
        # Save to local CSV file
        if os.path.exists("responses.csv"):
            existing = pd.read_csv("responses.csv")
            updated = pd.concat([existing, new_data], ignore_index=True)
        else:
            updated = new_data

        updated.to_csv("responses.csv", index=False)
        st.success("✅ Submission recorded successfully!")
    else:
        st.error("❌ Please fill in all fields.")


