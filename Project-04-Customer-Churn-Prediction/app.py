from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(
    open('customer_churn_model.pkl', 'rb')
)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    gender = int(request.form['gender'])
    SeniorCitizen = int(request.form['SeniorCitizen'])
    Partner = int(request.form['Partner'])
    Dependents = int(request.form['Dependents'])
    tenure = int(request.form['tenure'])

    PhoneService = int(request.form['PhoneService'])
    MultipleLines = int(request.form['MultipleLines'])
    InternetService = int(request.form['InternetService'])

    OnlineSecurity = int(request.form['OnlineSecurity'])
    OnlineBackup = int(request.form['OnlineBackup'])
    DeviceProtection = int(request.form['DeviceProtection'])
    TechSupport = int(request.form['TechSupport'])

    StreamingTV = int(request.form['StreamingTV'])
    StreamingMovies = int(request.form['StreamingMovies'])

    Contract = int(request.form['Contract'])
    PaperlessBilling = int(request.form['PaperlessBilling'])
    PaymentMethod = int(request.form['PaymentMethod'])

    MonthlyCharges = float(request.form['MonthlyCharges'])
    TotalCharges = float(request.form['TotalCharges'])

    features = [[
        gender,
        SeniorCitizen,
        Partner,
        Dependents,
        tenure,
        PhoneService,
        MultipleLines,
        InternetService,
        OnlineSecurity,
        OnlineBackup,
        DeviceProtection,
        TechSupport,
        StreamingTV,
        StreamingMovies,
        Contract,
        PaperlessBilling,
        PaymentMethod,
        MonthlyCharges,
        TotalCharges
    ]]

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Customer Likely to Churn"
    else:
        result = "Customer Likely to Stay"

    contract_map = {
        0: "Month-to-Month",
        1: "One Year",
        2: "Two Year"
    }

    payment_map = {
        0: "Bank Transfer Automatic",
        1: "Credit Card Automatic",
        2: "Electronic Check",
        3: "Mailed Check"
    }

    return render_template(
        'result.html',
        result=result,
        tenure=tenure,
        monthly_charges=MonthlyCharges,
        total_charges=TotalCharges,
        contract=contract_map[Contract],
        payment_method=payment_map[PaymentMethod]
    )


if __name__ == '__main__':
    app.run(debug=True)