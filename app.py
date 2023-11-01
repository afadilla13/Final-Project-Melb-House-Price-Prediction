from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
from flask import Flask, send_from_directory

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

    # Encoding for 'type' feature
    type_encoding = {
    'House': 0,
    'Townhouse': 1,
    'Unit': 2
    }
    encoded_type = type_encoding[data['type']]

    # Encoding for 'region' feature
    region_encoding = {
        'Eastern Metropolitan': 0,
        'Eastern Victoria': 1,
        'Northern Metropolitan': 2,
        'Northern Victoria': 3,
        'South-Eastern Metropolitan': 4,
        'Southern Metropolitan': 5,
        'Western Metropolitan': 6,
        'Western Victoria': 7,
    }
    encoded_region = region_encoding[data['region']]

    # Prepare data for prediction
    prediction_data = pd.DataFrame({
        'Rooms': [data['rooms']],
        'Type': [encoded_type],
        'Distance': [data['distance']],
        'Bathroom': [data['bathroom']],
        'Car': [data['garage']],
        'Region': [encoded_region]
    })

    # Make prediction
    prediction = model.predict(prediction_data)[0]
    formatted_prediction = "${:,.2f}".format(prediction)
    return jsonify(result=formatted_prediction)

if __name__ == '__main__':
    app.run(debug=True) 