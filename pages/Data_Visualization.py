import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


st.set_page_config(
    page_title="Data Visualization",
    layout="wide",
    page_icon="📊"
)

st.title("Data Visualization")

file_path = os.path.join(os.path.dirname(__file__), '../data_telco_customer_churn.csv')

# Load the dataset
data = pd.read_csv(file_path)

st.subheader("Original Data")
st.dataframe(data.reset_index(drop=True), use_container_width=True)

st.subheader("Data Visualization")

# Ensure Churn is categorized
if "Churn" in data.columns:
    data["Churn"] = data["Churn"].astype("category")

# Identify categorical columns for visualization
categorical_columns = data.select_dtypes(include=['object', 'category']).columns
categorical_columns = [col for col in categorical_columns if col != "Churn"]  # Exclude Churn itself

col1, col2 = None, None
for i, col in enumerate(categorical_columns):
    if i % 2 == 0:
        col1, col2 = st.columns(2)

    with (col1 if i % 2 == 0 else col2):
        st.write(f"Distribution of {col} with Churn as Hue")

        # Create the bar plot using Seaborn
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.countplot(data=data, x=col, hue="Churn", palette=['crimson','darkblue'], ax=ax)

        ax.set_title(f"Distribution of {col} by Churn")
        ax.set_xlabel("")
        ax.set_ylabel("Count")
        ax.legend(title="Churn")
        plt.xticks(rotation=0)

        st.pyplot(fig)
