import streamlit as st
import requests
import joblib
st.title("Diabeties Prediction app")
st.subheader("Machine Learning Model Demo")
st.markdown("Enter 10 features  and click ** Predict ** to get the prediction")
st.sidebar.title("About This App")

st.sidebar.write(
"""
This demo app uses:

• FastAPI backend  
• Scikit-learn ML model  
• Streamlit frontend  

The model predicts values based on user input features.
"""
)
features=[]
model = joblib.load("../backend/diabetes.pkl")


for i in range(10):
    value=st.number_input(f"Feature {i+1}",value=0.0)
    features.append(value)
if st.button("Predict"):

    try:
        with st.spinner("Generating prediction..."):
            prediction = model.predict([features])

        st.success(f"Prediction: {prediction[0]}")

    except Exception as e:
        st.error("Prediction failed.")