from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open('house_price_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    # Numerical Features
    area = int(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    stories = int(request.form['stories'])
    parking = int(request.form['parking'])

    # Binary Features
    mainroad = int(request.form['mainroad'])
    guestroom = int(request.form['guestroom'])
    basement = int(request.form['basement'])
    hotwaterheating = int(request.form['hotwaterheating'])
    airconditioning = int(request.form['airconditioning'])
    prefarea = int(request.form['prefarea'])

    # Furnishing Status
    furnishingstatus = request.form['furnishingstatus']

    # One-Hot Encoding (same as training)
    furnishingstatus_semi_furnished = 0
    furnishingstatus_unfurnished = 0

    if furnishingstatus == "semi-furnished":
        furnishingstatus_semi_furnished = 1

    elif furnishingstatus == "unfurnished":
        furnishingstatus_unfurnished = 1

    # Feature Vector
    features = [[
        area,
        bedrooms,
        bathrooms,
        stories,
        mainroad,
        guestroom,
        basement,
        hotwaterheating,
        airconditioning,
        parking,
        prefarea,
        furnishingstatus_semi_furnished,
        furnishingstatus_unfurnished
    ]]

    # Prediction
    prediction = model.predict(features)

    predicted_price = format(prediction[0], ",.2f")

    from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open('house_price_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    # Numerical Features
    area = int(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    stories = int(request.form['stories'])
    parking = int(request.form['parking'])

    # Binary Features
    mainroad = int(request.form['mainroad'])
    guestroom = int(request.form['guestroom'])
    basement = int(request.form['basement'])
    hotwaterheating = int(request.form['hotwaterheating'])
    airconditioning = int(request.form['airconditioning'])
    prefarea = int(request.form['prefarea'])

    # Furnishing Status
    furnishingstatus = request.form['furnishingstatus']

    # One-Hot Encoding (same as training)
    furnishingstatus_semi_furnished = 0
    furnishingstatus_unfurnished = 0

    if furnishingstatus == "semi-furnished":
        furnishingstatus_semi_furnished = 1

    elif furnishingstatus == "unfurnished":
        furnishingstatus_unfurnished = 1

    # Feature Vector
    features = [[
        area,
        bedrooms,
        bathrooms,
        stories,
        mainroad,
        guestroom,
        basement,
        hotwaterheating,
        airconditioning,
        parking,
        prefarea,
        furnishingstatus_semi_furnished,
        furnishingstatus_unfurnished
    ]]

    # Prediction
    prediction = model.predict(features)

    predicted_price = format(prediction[0], ",.2f")

    return render_template(
        'result.html',

        prediction=predicted_price,

        area=area,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        stories=stories,
        parking=parking,

        mainroad=mainroad,
        guestroom=guestroom,
        basement=basement,
        hotwaterheating=hotwaterheating,
        airconditioning=airconditioning,
        prefarea=prefarea,

        furnishingstatus=furnishingstatus
    )


if __name__ == '__main__':
    app.run(debug=True)