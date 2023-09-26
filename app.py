from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model1.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    Age = int(request.form.get('age'))
    Gender = request.form.get('Gender')
    Engineer = request.form.get('engineer')
    MBA = request.form.get('MBA')
    Work_Exp = int(request.form.get('Work Experience'))
    Salary = float(request.form.get('Salary'))
    Distance = float(request.form.get('Distance'))
    License = request.form.get('license')

    if Gender=='Male':
        Gender=1
    else:
        Gender=0

    if Engineer=='Yes':
        Engineer=1
    else:
        Engineer=0

    if MBA=='Yes':
        MBA=1
    else:
        MBA=0

    if License=='Yes':
        License=1
    else:
        License=0

    col=["Age", "Gender", "Engineer", "MBA", "Work Exp", "Salary", "Distance", "License"]
    output = model.predict(pd.DataFrame(np.array([Age, Gender, Engineer, MBA, Work_Exp, Salary, Distance,License]).reshape(1, 8),columns=col))[0]
    print(output)
    if output == 0:
        result = "MODE OF TRANSPORT IS CAR"
    elif output== 1:
        result = "MODE OF TRANSPORT IS 2-Wheeler"
    elif output==2:
        result="MODE OF TRANSPORT IS PUBLIC TRANSPORT"
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
