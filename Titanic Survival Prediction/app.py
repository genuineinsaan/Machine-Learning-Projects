from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(
    open('titanic_survival_model.pkl', 'rb')
)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    pclass = int(request.form['pclass'])
    sex = int(request.form['sex'])
    age = float(request.form['age'])
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])
    fare = float(request.form['fare'])
    embarked = int(request.form['embarked'])

    features = [[
        pclass,
        sex,
        age,
        sibsp,
        parch,
        fare,
        embarked
    ]]

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Survived"
    else:
        result = "Did Not Survive"

    return render_template(
        'result.html',
        result=result,
        pclass=pclass,
        sex="Female" if sex == 1 else "Male",
        age=age,
        sibsp=sibsp,
        parch=parch,
        fare=f"₹ {fare:,.2f}",
        embarked={
            0: "Southampton (S)",
            1: "Cherbourg (C)",
            2: "Queenstown (Q)"
        }[embarked]
    )

if __name__ == '__main__':
    app.run(debug=True)
