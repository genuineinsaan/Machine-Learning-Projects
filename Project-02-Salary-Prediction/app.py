from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(
    open('salary_prediction_model.pkl', 'rb')
)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    experience = float(request.form['experience'])

    prediction = model.predict([[experience]])

    predicted_salary = format(prediction[0], ",.2f")

    return render_template(
        'result.html',
        prediction=predicted_salary,
        experience=experience
    )

if __name__ == '__main__':
    app.run(debug=True)