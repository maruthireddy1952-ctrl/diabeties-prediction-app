#Diabeties Prediction App

This Project demonstrates a deployable machine learning application.

Tech stack:
-Scikit-learn (ML Model)
-FastAPI (backend API)
-Pydantic(data Validation)
-Streamlit (frontend UI)

Architecture:
User-> Stremlit UI -> FastAPI -> ML Model -> Prediction

How to run:
1. Start the API
uvicorn filename:appname --reload

2. Run frontend
streamlit run filename.py"# diabeties-prediction-app" 
