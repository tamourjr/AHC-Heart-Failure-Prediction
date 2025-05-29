
import streamlit as st
import pandas as pd
import appstreamdash


df = pd.read_csv("heart.csv")
df['HeartDisease'] = df['HeartDisease'].map({0: 'No', 1: 'Yes'})
df['Sex'] = df['Sex'].map({'M': 'Male', 'F': 'Female'})



st.set_page_config(layout="wide")
st.title(" Heart Disease Dashboard")

# Graphs
st.plotly_chart(appstreamdash.hist_sex_disease(df))
st.plotly_chart(appstreamdash.box_age_disease(df))
st.plotly_chart(appstreamdash.scatter_age_maxhr(df))
st.plotly_chart(appstreamdash.hist_chest_pain(df))
st.plotly_chart(appstreamdash.violin_bp_by_disease(df))
st.plotly_chart(appstreamdash.scatter_chol_age(df))
st.plotly_chart(appstreamdash.treemap_gender_chestpain(df))
st.plotly_chart(appstreamdash.hist_chestpain_gender(df))
st.plotly_chart(appstreamdash.violin_maxhr_gender(df))
st.plotly_chart(appstreamdash.bar_chestpain_gender(df))
st.plotly_chart(appstreamdash.hist_st_slope(df))
st.plotly_chart(appstreamdash.pie_chestpain(df))

# Medical Insights Section
st.subheader("Medical Insights")

col1, col2 = st.columns(2)

with col1:
    st.info("• Males are more likely to suffer from heart disease than females, especially in the 50+ age group.")
    st.warning("• ASY (Asymptomatic) chest pain is a strong indicator of silent heart issues.")
    st.success("• Flat ST Slope is associated with abnormal heart behavior and reduced blood flow.")
    st.info("• Fasting Blood Sugar above 120 mg/dL may indicate a higher risk of heart disease.")

with col2:
    st.error("• High cholesterol (above 240) is frequently observed in patients with heart disease.")
    st.warning("• MaxHR below 120 is often linked to reduced cardiac output in heart disease cases.")
    st.error("• Resting Blood Pressure above 140 mmHg indicates a risk of hypertension.")
    st.info("• Heart disease is more common in patients with exercise-induced angina.")

# Case Study Simulation
st.subheader("Case Study Simulation")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Patient Data")
    st.markdown("""
    - **Age:** 63  
    - **Sex:** Male  
    - **Chest Pain:** ASY  
    - **ST Slope:** Flat  
    - **Cholesterol:** 280 mg/dL  
    - **MaxHR:** 110 bpm
    """)
    st.markdown("### Conclusion")
    st.warning("High risk of heart disease.")
    st.info("Recommended: ECG, stress test, and cardiac consultation.")


with col2:
    st.markdown("### Evaluation")
    st.markdown("""
    - ASY chest pain suggests silent cardiac symptoms.
    - Flat ST slope is concerning for ischemia.
    - Cholesterol is significantly elevated.
    - MaxHR is low, potentially indicating reduced cardiac response.
    """)
    

st.subheader(" Heart Disease Prediction")
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp_type = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
chol = st.slider("Cholesterol", 100, 400, 200)
max_hr = st.slider("Max Heart Rate", 60, 200, 130)

if st.button("Predict"):
    # Convert to same format as model training
    input_df = pd.DataFrame({
        "Age": [age],
        "Sex": [1 if sex == "Male" else 0],
        "ChestPainType": [cp_type],
        "Cholesterol": [chol],
        "MaxHR": [max_hr]
    })
    # model = joblib.load("model.pkl")
    # prediction = model.predict(input_df)
    st.success("⚠️ High Risk of Heart Disease")  # Replace with actual prediction


# Interactive Insights by Chest Pain Type
st.subheader(" Explore Insights by Chest Pain Type")
selected_pain = st.selectbox("Select Chest Pain Type", df["ChestPainType"].unique())

chest_insights = {
    "ASY": "🔴 ASY (Asymptomatic) pain often goes unnoticed by patients but is strongly associated with high risk of heart disease.",
    "NAP": "🟡 NAP (Non-Anginal Pain) typically relates to non-cardiac issues but should still be monitored.",
    "ATA": "🟠 ATA (Atypical Angina) may indicate moderate heart stress and warrants follow-up tests.",
    "TA": "🟢 TA (Typical Angina) is a classic indicator of heart issues but varies based on other factors."
}

st.markdown(f"**Insight:** {chest_insights[selected_pain]}")

# Interactive Gender-Based Insights
st.subheader(" Gender-Based Heart Disease Insight")
selected_gender = st.radio("Choose Gender:", ["Male", "Female"])

if selected_gender == "Male":
    st.markdown("🔴 **Males show a significantly higher rate of heart disease in the dataset. Clinical attention to cholesterol and ST slope is recommended.**")
else:
    st.markdown("🟢 **Females have lower rates, but symptoms are often less typical. Early detection may be more difficult.**")
