import streamlit as st
from PIL import Image  # For loading and displaying images

# Configure the page
st.set_page_config(
    page_title="Model Performance Evaluation",
    layout="wide",
    page_icon="📈"
)

# Page title
st.title("📊 Model Performance Evaluation")

# Subheader for explanation
st.subheader("Explore the performance metrics of the model:")

st.write("""
This page presents visualizations of key evaluation metrics for the model:
- Confusion Matrix
- ROC Curve
- Churn Cost
- Feature Importance
""")

# Load and display the pictures
# Paths to the images in the "assets" folder
confusion_matrix_path = "./Model/Confusion Matrix.png"
roc_curve_path = "./Model/PR Curve when Testing data test in Training Model.png"
feature_importance_path = "./Model/Top 10 feature importances.png"
churn_path = "./Model/Cost in Telco Customer Churn.png"

# Section 1: Confusion Matrix
st.write("### Confusion Matrix")
confusion_img = Image.open(confusion_matrix_path)
st.image(confusion_img, caption="Confusion Matrix")

# Section 2: ROC Curve
st.write("### ROC Curve")
roc_curve_img = Image.open(roc_curve_path)
st.image(roc_curve_img, caption="ROC Curve")

# Section 3: Churn Cost
st.write("### Churn Cost")
st.write("")
feature_importance_img = Image.open(churn_path)
st.image(feature_importance_img, caption="Churn Cost")

# Section 4: Feature Importance
st.write("### Feature Importance")
feature_importance_img = Image.open(feature_importance_path)
st.image(feature_importance_img, caption="Feature Importance")

