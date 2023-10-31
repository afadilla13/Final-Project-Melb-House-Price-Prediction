from flask import Flask, render_template, request, jsonify
import pickle

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
        'type0': 0,
        'type1': 1,
        'type2': 2,
        # Add other encodings if there are more types
    }
    encoded_type = type_encoding[data['type']]

    # Encoding for 'region' feature
    region_encoding = {
        'region0': 0,
        'region1': 1,
        'region2': 2,
        'region3': 3,
        'region4': 4,
        'region5': 5,
        'region6': 6,
        'region7': 7,
        # Add other encodings if there are more regions
    }
    encoded_region = region_encoding[data['region']]

    # Prepare data for prediction
    prediction_data = [
        data['rooms'],
        encoded_type,
        data['bathroom'],
        data['garage'],
        data['distance'],
        encoded_region  # Use the encoded value
    ]

    # Make prediction
    prediction = model.predict([prediction_data])[0]
    formatted_prediction = "${:,.2f}".format(prediction)
    return jsonify(result=formatted_prediction)

if __name__ == '__main__':
    app.run(debug=True) 