# **Telco Customer Churn Analysis**

This repository showcases my skills as a **Data Scientist**, combining **machine learning**, **data visualization**, and **application development** to address a critical business problem: **Customer Churn Prediction** in the telecommunications industry. The project demonstrates my ability to extract actionable insights, build predictive models, and develop interactive solutions for real-world challenges.

---

## **Project Overview**

### **Problem Statement**
Customer churn is a major challenge for telecommunication companies, leading to significant revenue loss and increased customer acquisition costs. Predicting and understanding customer churn enables businesses to implement targeted retention strategies and improve customer satisfaction.

### **Solution**
This project focuses on:
1. **Analyzing customer data** to uncover key drivers of churn.
2. **Building predictive models** to accurately identify at-risk customers.
3. **Developing an interactive Streamlit application** to enable users to explore insights, evaluate model performance, and make predictions.

---

## **Repository Highlights**

This repository demonstrates the complete Data Science workflow, including **data analysis**, **model development**, and **deployment**. Below is an overview of the key files:

### **Main Files**
- **`Capstone3_Telco.ipynb`**:  
  A Jupyter Notebook containing the entire Data Science pipeline:
  - Exploratory Data Analysis (EDA)
  - Feature Engineering
  - Model Training and Evaluation
  - Insights and Recommendations

- **`Homepage.py`**:  
  The **Streamlit-based homepage**, introducing the project and serving as a navigation hub for the application.

- **`README.md`**:  
  This document, providing a detailed overview of the project and its structure.

- **`Telco Customer Churn.docx`**:  
  A formal project report summarizing analysis, results, and recommendations.

- **`data_telco_customer_churn.csv`**:  
  The dataset used in this project, containing customer demographics, service usage, and contract details.

- **`model.pkl`**:  
  The serialized machine learning model for deployment in the Streamlit app.

---

### **Streamlit Pages**

This project includes **Streamlit-powered pages** for interactive exploration and prediction:

1. **`Data_Visualization.py`**:  
   Provides interactive visualizations to explore customer patterns and trends related to churn.

2. **`Model_Performance_Evaluation.py`**:  
   Displays evaluation metrics and visualizations, such as the Confusion Matrix, Precision-Recall Curve, and ROC-AUC.

3. **`Model_Prediction.py`**:  
   Allows users to input new customer data and receive churn predictions using the trained model.

---

### **Model Evaluation Visualizations**

- **`Confusion Matrix.png`**: Visual breakdown of prediction outcomes.  
- **`Cost in Telco Customer Churn.png`**: Graph showing the financial impact of prediction errors.  
- **`PR Curve when Testing Data Test in Training Model.png`**: Precision-Recall Curve for the test dataset.  
- **`Top 10 Feature Importances.png`**: Bar chart showcasing the most significant features driving churn.

---

## **Key Skills Demonstrated**

1. **Data Wrangling and Cleaning**  
   - Handled missing data, encoded categorical variables, and scaled numerical features.
   - Balanced class distribution to improve model performance.

2. **Exploratory Data Analysis (EDA)**  
   - Visualized customer data to uncover trends and correlations using **Seaborn** and **Matplotlib**.

3. **Machine Learning**  
   - Trained classification models like **Logistic Regression**, **Random Forest**, and **Gradient Boosting**.
   - Performed hyperparameter tuning using **GridSearchCV**.

4. **Model Evaluation**  
   - Used metrics like **Precision**, **Recall**, **F1-Score**, and **ROC-AUC** to assess model effectiveness.
   - Prioritized **Recall** to minimize false negatives.

5. **Deployment and Visualization**  
   - Built an interactive **Streamlit** application for accessible insights and predictions.
   - Designed modular Streamlit pages for flexible and user-friendly navigation.

---

## **Prediction Modes in Streamlit Application**

The **Model Prediction** page in this project offers three distinct modes for predicting customer churn, catering to different user requirements. Below is a detailed explanation of each mode:

### **1. Single Prediction**
This mode allows users to predict churn for an individual customer by manually inputting their details.

- **Steps:**
  1. Use the **sidebar** to input customer attributes like tenure, online security, monthly charges, etc.
  2. Click the **Predict** button to see the result.
- **Output:**
  - A clear and color-coded result:  
    - **🚨 "The customer will churn!"** (Red)  
    - **✅ "The customer will NOT churn!"** (Green)  
  - Displays customer details for transparency.

This mode is ideal for analyzing churn risk for individual cases or hypothetical scenarios.

---

### **2. Batch Prediction (File Upload)**
This mode supports predicting churn for multiple customers at once by uploading a CSV file containing customer data.

- **Steps:**
  1. Prepare a CSV file with customer attributes. Ensure it includes the required columns:
     - `Dependents`, `tenure`, `OnlineSecurity`, `OnlineBackup`, `InternetService`,  
       `DeviceProtection`, `TechSupport`, `Contract`, `PaperlessBilling`, `MonthlyCharges`.
  2. Upload the CSV file via the provided uploader.
  3. Click **Predict Batch** to generate predictions.
- **Output:**
  - A table displaying each customer's details along with the **Churn_Prediction** column.
  - Option to **download predictions** as a CSV file.

This mode is designed for processing large datasets efficiently.

---

### **3. Batch Prediction (Manual Input)**
This mode enables users to input data for multiple customers directly in the app.

- **Steps:**
  1. Specify the number of customers to input.
  2. Fill out the details for each customer in the form provided.
  3. Click **Predict Batch (Manual)** to generate predictions.
- **Output:**
  - A table displaying the manually entered data along with the **Churn_Prediction** column.

This mode is useful for testing small datasets or when data entry flexibility is needed.

---

### **Common Features Across Modes**
- **Interactive Data Entry:** User-friendly forms and inputs to capture data.
- **Real-time Predictions:** Leverages the trained model (`model.pkl`) for instant results.
- **Churn Indicators:** Displays whether a customer is likely to churn (`Yes`) or not (`No`).
- **Ease of Use:** No programming knowledge required to operate.

These prediction modes ensure flexibility and scalability, allowing users to address both individual and bulk prediction needs effectively.

---

## **How to Run the Project**

### **Prerequisites**
Install Python 3.x and the following libraries:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- streamlit
- xgboost
- lightgbm
- pickle
- joblib
- imblearn

### **Steps to Run**  
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telco-churn-analysis.git
   cd telco-churn-analysis
