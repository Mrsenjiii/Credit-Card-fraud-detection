from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        LIMIT_BAL = request.form.get('LIMIT_BAL')
        SEX = request.form.get('SEX')
        AGE = request.form.get('AGE')
        PAY_1 = request.form.get('PAY_1')
        PAY_2 = request.form.get('PAY_2')
        PAY_3 = request.form.get('PAY_3')
        PAY_4 = request.form.get('PAY_4')
        PAY_5 = request.form.get('PAY_5')
        PAY_6 = request.form.get('PAY_6')
        BILL_AMT1 = request.form.get('BILL_AMT1')
        BILL_AMT2 = request.form.get('BILL_AMT2')
        BILL_AMT3 = request.form.get('BILL_AMT3')
        BILL_AMT4 = request.form.get('BILL_AMT4')
        BILL_AMT5 = request.form.get('BILL_AMT5')
        BILL_AMT6 = request.form.get('BILL_AMT6')
        PAY_AMT1 = request.form.get('PAY_AMT1')
        PAY_AMT2 = request.form.get('PAY_AMT2')
        PAY_AMT3 = request.form.get('PAY_AMT3')
        PAY_AMT4 = request.form.get('PAY_AMT4')
        PAY_AMT5 = request.form.get('PAY_AMT5')
        PAY_AMT6 = request.form.get('PAY_AMT6')
        EDUCATION_Grade_School = request.form.get('EDUCATION_Grade_School')
        EDUCATION_High_School = request.form.get('EDUCATION_High_School')
        EDUCATION_Others = request.form.get('EDUCATION_Others')
        EDUCATION_University = request.form.get('EDUCATION_University')
        MARRIAGE_Married = request.form.get('MARRIAGE_Married')
        MARRIAGE_Others = request.form.get('MARRIAGE_Others')
        MARRIAGE_Single = request.form.get('MARRIAGE_Single')

        if not all([LIMIT_BAL, SEX, AGE, 
                    PAY_1, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
                    BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
                    PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6,
                    EDUCATION_Grade_School, EDUCATION_High_School, EDUCATION_Others, EDUCATION_University,
                    MARRIAGE_Married, MARRIAGE_Others,MARRIAGE_Single]):
            return render_template('home.html', error="Please fill in all fields.")

        try:
            LIMIT_BAL = float(LIMIT_BAL)
            SEX = int(SEX)
            AGE = int(AGE)
            PAY_1 = int(PAY_1)
            PAY_2 = int(PAY_2)
            PAY_3 = int(PAY_3)
            PAY_4 = int(PAY_4)
            PAY_5 = int(PAY_5)
            PAY_6 = int(PAY_6)
            BILL_AMT1 = float(BILL_AMT1)
            BILL_AMT2 = float(BILL_AMT2)
            BILL_AMT3 = float(BILL_AMT3)
            BILL_AMT4 = float(BILL_AMT4)
            BILL_AMT5 = float(BILL_AMT5)
            BILL_AMT6 = float(BILL_AMT6)
            PAY_AMT1 = float(PAY_AMT1)
            PAY_AMT2 = float(PAY_AMT2)
            PAY_AMT3 = float(PAY_AMT3)
            PAY_AMT4 = float(PAY_AMT4) 
            PAY_AMT5 = float(PAY_AMT5)
            PAY_AMT6 = float(PAY_AMT6)

            education = 0 
            if EDUCATION_Grade_School == '1':
                education = 1
            elif EDUCATION_High_School == '1':
                education = 2
            elif EDUCATION_University == '1':
                education = 3
            elif EDUCATION_Others == '1':
                education = 4

            marriage = 0 
            if MARRIAGE_Married == '1':
                marriage = 1
            elif MARRIAGE_Single == '1':
                marriage = 2
            elif MARRIAGE_Others == '1':
                marriage = 3

            if LIMIT_BAL < 0:
                raise ValueError("Limit balance cannot be negative.")
            if AGE < 18:
                raise ValueError("Age must be 18 or older.")

        except ValueError as e:
            return render_template('home.html', error=f"Invalid data format: {str(e)}")

        data = [[LIMIT_BAL, SEX, AGE, 
                    PAY_1, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
                    BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
                    PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6,
                    EDUCATION_Grade_School, EDUCATION_High_School, EDUCATION_Others, EDUCATION_University,
                    MARRIAGE_Married, MARRIAGE_Others, MARRIAGE_Single]]

        pred_df = pd.DataFrame(data, columns=['LIMIT_BAL', 'SEX', 'AGE', 
                                                'PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 
                                                'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 
                                                'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6',
                                                'EDUCATION_Grade_School', 'EDUCATION_High_School', 'EDUCATION_Others', 'EDUCATION_University', 
                                                'MARRIAGE_Married', 'MARRIAGE_Others', 'MARRIAGE_Single',])

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        if results[0] == 1:
            prediction = "Default in the next month"
        elif results[0] == 0:
            prediction = "Not be Default in the next month"
        else:
            prediction = "Prediction Error"

        return render_template('home.html', prediction=prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0')