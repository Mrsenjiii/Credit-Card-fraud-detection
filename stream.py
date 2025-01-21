import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline

st.title("Credit Card Default Prediction")

LIMIT_BAL = st.number_input("LIMIT_BAL (Credit Limit):", min_value=0)
SEX = st.radio("SEX (Gender):", options=["Male", "Female"], index=0)
AGE = st.number_input("AGE:", min_value=18, format="%i")
pay_options = range(-1, 9)
PAY_1 = st.selectbox("PAY_1 (Repayment Status in September):", options=pay_options)
PAY_2 = st.selectbox("PAY_2 (Repayment Status in August):", options=pay_options)
PAY_3 = st.selectbox("PAY_3 (Repayment Status in July):", options=pay_options)
PAY_4 = st.selectbox("PAY_4 (Repayment Status in June):", options=pay_options)
PAY_5 = st.selectbox("PAY_5 (Repayment Status in May):", options=pay_options)
PAY_6 = st.selectbox("PAY_6 (Repayment Status in April):", options=pay_options)
BILL_AMT1 = st.number_input("BILL_AMT1 (Bill Amount in September):")
BILL_AMT2 = st.number_input("BILL_AMT2 (Bill Amount in August):")
BILL_AMT3 = st.number_input("BILL_AMT3 (Bill Amount in July):")
BILL_AMT4 = st.number_input("BILL_AMT4 (Bill Amount in June):")
BILL_AMT5 = st.number_input("BILL_AMT5 (Bill Amount in May):")
BILL_AMT6 = st.number_input("BILL_AMT6 (Bill Amount in April):")
PAY_AMT1 = st.number_input("PAY_AMT1 (Previous Payment Amount in September):")
PAY_AMT2 = st.number_input("PAY_AMT2 (Previous Payment Amount in August):")
PAY_AMT3 = st.number_input("PAY_AMT3 (Previous Payment Amount in July):")
PAY_AMT4 = st.number_input("PAY_AMT4 (Previous Payment Amount in June):")
PAY_AMT5 = st.number_input("PAY_AMT5 (Previous Payment Amount in May):")
PAY_AMT6 = st.number_input("PAY_AMT6 (Previous Payment Amount in April):")

EDUCATION_Grade_School = st.radio("EDUCATION_Grade_School:", options=["Yes", "No"], index=1)
EDUCATION_High_School = st.radio("EDUCATION_High_School:", options=["Yes", "No"], index=1)
EDUCATION_Others = st.radio("EDUCATION_Others:", options=["Yes", "No"], index=1)
EDUCATION_University = st.radio("EDUCATION_University:", options=["Yes", "No"], index=1)

MARRIAGE_Married = st.radio("MARRIAGE_Married:", options=["Yes", "No"], index=1)
MARRIAGE_Others = st.radio("MARRIAGE_Others:", options=["Yes", "No"], index=1)
MARRIAGE_Single = st.radio("MARRIAGE_Single:", options=["Yes", "No"], index=1)

SEX = 1 if SEX == "Male" else 0
EDUCATION_Grade_School = 1 if EDUCATION_Grade_School == "Yes" else 0
EDUCATION_High_School = 1 if EDUCATION_High_School == "Yes" else 0
EDUCATION_Others = 1 if EDUCATION_Others == "Yes" else 0
EDUCATION_University = 1 if EDUCATION_University == "Yes" else 0
MARRIAGE_Married = 1 if MARRIAGE_Married == "Yes" else 0
MARRIAGE_Others = 1 if MARRIAGE_Others == "Yes" else 0
MARRIAGE_Single = 1 if MARRIAGE_Single == "Yes" else 0

if st.button("Predict"):
    data = [[LIMIT_BAL, SEX, AGE, PAY_1, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
                BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
                PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6,
                EDUCATION_Grade_School, EDUCATION_High_School, EDUCATION_Others, EDUCATION_University,
                MARRIAGE_Married, MARRIAGE_Others, MARRIAGE_Single]]
    pred_df = pd.DataFrame(data, columns=['LIMIT_BAL', 'SEX', 'AGE', 'PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6',
                                            'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6',
                                            'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6',
                                            'EDUCATION_Grade_School', 'EDUCATION_High_School', 'EDUCATION_Others', 'EDUCATION_University',
                                            'MARRIAGE_Married', 'MARRIAGE_Others','MARRIAGE_Single'])

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    if results[0] == 1:
        st.write("Prediction: Default in the next month")
    elif results[0] == 0:
        st.write("Prediction: Not be Default in the next month")
    else:
        st.write("Prediction Error")

# if __name__ == "__main__":
#     main()