import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="Machine Learning Model",
    layout="wide",
    page_icon="🧠"
)

st.title("Model Prediction")

model_path = os.path.join(os.path.dirname(__file__), '../model.pkl')

# Load the trained model
model = joblib.load(model_path)

# Toggle between prediction modes
prediction_mode = st.radio(
    "Select Prediction Mode",
    ("Single Prediction", "Batch Prediction (File Upload)", "Batch Prediction (Manual Input)")
)

if prediction_mode == "Single Prediction":
    st.sidebar.subheader("Input Customer Details to Predict Churn")

    # Collect user inputs for the relevant features
    dependents = st.sidebar.selectbox("Dependents", ("Yes", "No"))
    tenure = st.sidebar.slider("Tenure (months)", 0, 72, 1)
    online_security = st.sidebar.selectbox("Online Security", ("Yes", "No", "No internet service"))
    online_backup = st.sidebar.selectbox("Online Backup", ("Yes", "No", "No internet service"))
    internet_service = st.sidebar.selectbox("Internet Service", ("DSL", "Fiber optic", "No"))
    device_protection = st.sidebar.selectbox("Device Protection", ("Yes", "No", "No internet service"))
    tech_support = st.sidebar.selectbox("Tech Support", ("Yes", "No", "No internet service"))
    contract = st.sidebar.selectbox("Contract", ("Month-to-month", "One year", "Two year"))
    paperless_billing = st.sidebar.selectbox("Paperless Billing", ("Yes", "No"))
    monthly_charges = st.sidebar.number_input("Monthly Charges", min_value=0.0, step=.5)

    # Prepare input data for prediction
    input_data = {
        "Dependents": dependents,
        "tenure": tenure,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "InternetService": internet_service,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "MonthlyCharges": monthly_charges,
    }

    input_df = pd.DataFrame([input_data])

    # Display input data
    st.subheader("Customer Details")
    st.write(input_df)

    # Predict churn for the single input
    if st.button("Predict"):
        churn = model.predict(input_df)  # Using the model pipeline to predict
        churn_result = "Yes" if churn[0] == 1 else "No"

        # Highlighted Prediction Display
        if churn_result == "Yes":
            st.markdown(f"<h2 style='color: red; text-align: center;'>🚨 Prediction: The customer will churn! 🚨</h2>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h2 style='color: green; text-align: center;'>✅ Prediction: The customer will NOT churn ✅</h2>", unsafe_allow_html=True)

elif prediction_mode == "Batch Prediction (File Upload)":
    st.subheader("Upload Batch Data for Prediction")

    # Upload a CSV file for batch prediction
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        batch_data = pd.read_csv(uploaded_file)

        # Display the uploaded data
        st.subheader("Uploaded Data")
        st.write(batch_data)

        # Check if required columns are present
        required_columns = [
            "Dependents", "tenure", "OnlineSecurity", "OnlineBackup", "InternetService",
            "DeviceProtection", "TechSupport", "Contract", "PaperlessBilling", "MonthlyCharges"
        ]

        if all(column in batch_data.columns for column in required_columns):
            # Predict churn for the batch input using the model pipeline
            if st.button("Predict Batch"):
                predictions = model.predict(batch_data)  # Using the model pipeline to predict
                batch_data["Churn_Prediction"] = ["Yes" if pred == 1 else "No" for pred in predictions]

                st.subheader("Prediction Results")
                st.write(batch_data)

                # Option to download results
                csv = batch_data.to_csv(index=False).encode('utf-8')
                st.download_button("Download Predictions", data=csv, file_name="predictions.csv", mime="text/csv")
        else:
            st.write("Error: Uploaded CSV does not contain all required columns.")

elif prediction_mode == "Batch Prediction (Manual Input)":
    st.subheader("Manual Input for Batch Prediction")

    # Set the number of rows for manual batch input
    num_rows = st.number_input("Number of Customers to Input", min_value=1, max_value=100, step=1, value=1)
    
    # Create an empty list to collect manual input data
    manual_data_list = []

    # Loop to collect inputs for each customer
    for i in range(num_rows):
        st.markdown(f"**Customer {i + 1} Details**")
        dependents = st.selectbox(f"Dependents (Customer {i + 1})", ("Yes", "No"), key=f"dependents_{i}")
        tenure = st.slider(f"Tenure (Customer {i + 1})", 0, 72, 1, key=f"tenure_{i}")
        online_security = st.selectbox(f"Online Security (Customer {i + 1})", ("Yes", "No", "No internet service"), key=f"online_security_{i}")
        online_backup = st.selectbox(f"Online Backup (Customer {i + 1})", ("Yes", "No", "No internet service"), key=f"online_backup_{i}")
        internet_service = st.selectbox(f"Internet Service (Customer {i + 1})", ("DSL", "Fiber optic", "No"), key=f"internet_service_{i}")
        device_protection = st.selectbox(f"Device Protection (Customer {i + 1})", ("Yes", "No", "No internet service"), key=f"device_protection_{i}")
        tech_support = st.selectbox(f"Tech Support (Customer {i + 1})", ("Yes", "No", "No internet service"), key=f"tech_support_{i}")
        contract = st.selectbox(f"Contract (Customer {i + 1})", ("Month-to-month", "One year", "Two year"), key=f"contract_{i}")
        paperless_billing = st.selectbox(f"Paperless Billing (Customer {i + 1})", ("Yes", "No"), key=f"paperless_billing_{i}")
        monthly_charges = st.number_input(f"Monthly Charges (Customer {i + 1})", min_value=0.0, step=0.5, key=f"monthly_charges_{i}")
        
        # Append customer data to the list
        manual_data_list.append({
            "Dependents": dependents,
            "tenure": tenure,
            "OnlineSecurity": online_security,
            "OnlineBackup": online_backup,
            "InternetService": internet_service,
            "DeviceProtection": device_protection,
            "TechSupport": tech_support,
            "Contract": contract,
            "PaperlessBilling": paperless_billing,
            "MonthlyCharges": monthly_charges
        })

    # Convert the list of dictionaries to a DataFrame
    manual_data = pd.DataFrame(manual_data_list)

    st.subheader("Manual Batch Data")
    st.write(manual_data)

    # Predict churn for the manual batch input
    if st.button("Predict Batch (Manual)"):
        predictions = model.predict(manual_data)  # Using the model pipeline to predict
        manual_data["Churn_Prediction"] = ["Yes" if pred == 1 else "No" for pred in predictions]

        st.subheader("Prediction Results")
        st.write(manual_data)
