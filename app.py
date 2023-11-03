from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
with open('Trained_Model/model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    data = request.get_json(force=True)

    # Prepare data for prediction
    prediction_data = pd.DataFrame({
        'Suburb': [data['suburb']],
        'Rooms': [data['rooms']],
        'Type': [data['type']],
        'Distance': [data['distance']],
        'Bathroom': [data['bathroom']],
        'Car': [data['garage']],
        'Region': [data['region']]
    })

    # Make prediction
    prediction = model.predict(prediction_data)[0]
    formatted_prediction = "${:,.2f}".format(prediction)
    return jsonify(result=formatted_prediction)

if __name__ == '__main__':
    app.run(debug=True) 