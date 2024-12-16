import streamlit as st

st.set_page_config(
    page_title="Telco Customer Churn Analysis",
    layout="wide",
    page_icon="🔍"
)

st.title("🌟Welcome to Telco Customer Churn Analysis🌟")
st.write("Use the sidebar to navigate between pages.")

st.header("Background on Customer Churn in Telecom 📝")
st.write("""
Customer churn, also known as customer attrition, refers to the phenomenon where customers stop using a company’s services or products. 

In the telecommunications industry, churn is a critical issue, as it directly impacts revenue and growth. Telecom companies often invest heavily in acquiring new customers, but it’s more cost-effective to retain existing ones. 

The challenge is identifying which customers are likely to churn before they leave, and taking steps to retain them. Factors such as customer satisfaction, service quality, contract type, and pricing often influence a customer's decision to stay or leave.

This project aims to analyze the factors contributing to churn, predict which customers are at risk of leaving, and provide actionable insights to reduce churn and optimize customer retention strategies.
""")

st.header("What Can You Explore?🚀")
st.write("""
This app allows you to predict **which customers are most likely to churn** based on a variety of features. By using these features, such as contract type, monthly charges, and customer tenure, the model estimates whether a customer will stay with the company or leave.

Here’s how you can interact with the app:

- **Input customer data**: Provide details such as whether the customer has dependents, the type of contract they have, and how long they’ve been with the company.
- **Get churn prediction**: Based on your input, the app will predict whether the customer is likely to churn (leave) or stay with the company.
- **Explore predictions based on key features**: Understand how each feature impacts the churn likelihood and how changing certain customer details could influence their risk of churning.

The app uses a machine learning model that has been trained on historical customer data to make these predictions. Use the input form to see the churn prediction for a specific customer, helping you identify high-risk customers and take actions to retain them.
""")

st.write("---")
st.write("Made by Kevin Rio Harristyando")