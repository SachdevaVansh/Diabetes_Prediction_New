from flask import Flask,request,app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd

application = Flask(__name__)
app=application

## Route for homepage

@app.route("/")
def index():
    return render_template('index.html')

## Route for Single data point prediction
@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    result=''

    if request.method=='POST':

        Preganancies=int(request.form.get("Pregagnancies"))
        Glucose=float(request.form.get('Glucose'))
        BloodPressure=float(request.form.get('BloodPressure'))
        SkinThickness=float(request.form.get('SkinThickness'))
        Insulin=float(request.form.get('Insulin'))
        BMI=float(request.form.get('BMI'))
        DiabetesPedigreeFunction=float(request.form.get('DiabetesPedigreeFunction'))
        Age=float(request.form.get('Age'))

        new_data=scaler.transform([[Pregagnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        predict=model.predict(new_data)

        if predict[0]==1:
            result='Diabeteic'
        else:
            result='Non-Diabetic'

        return render_template('single_prediction.html',result=result)

    else:
        return render_template('home.html')        

    

if __name__=="__main__":
    app.run(host="0.0.0.0")
