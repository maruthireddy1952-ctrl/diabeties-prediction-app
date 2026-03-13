import streamlit as st
import requests

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

for i in range(10):
    value=st.number_input(f"Feature {i+1}",value=0.0)
    features.append(value)
if st.button("Predict"):
    if len(features) !=10 or 0.0 in features :
        st.error("Please enter all 10 features.")
    else:
        try:
            url="http://127.0.0.1:8000/predict"
            with st.spinner("Generating prediction..."):
                response=requests.post(url,json={"features":features})
                result=response.json()
                st.success(f"Prediction: {result['Prediction']}")
        except Exception as e:
            st.error("API not responding.Make sure FastAPI server is running.")