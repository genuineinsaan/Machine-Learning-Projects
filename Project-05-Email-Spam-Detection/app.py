from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(
    open('spam_model.pkl', 'rb')
)

vectorizer = pickle.load(
    open('tfidf_vectorizer.pkl', 'rb')
)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    message = request.form['message']

    message_vector = vectorizer.transform(
        [message]
    )

    prediction = model.predict(
        message_vector
    )

    if prediction[0] == 1:
        result = "Spam Message"
        prediction_class = "spam"

    else:
        result = "Not Spam"
        prediction_class = "ham"

    return render_template(
        'result.html',
        result=result,
        message=message,
        prediction_class=prediction_class
    )


if __name__ == '__main__':
    app.run(debug=True)