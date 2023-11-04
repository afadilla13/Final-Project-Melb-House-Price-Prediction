from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

# Initialize a new Flask application.
app = Flask(__name__)

# Load the pre-trained model from a .pkl file.
with open('Trained_Model/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the root route which renders the 'index.html' template.
@app.route('/')
def index():
    return render_template('index.html')

# Define the '/predict' route which accepts POST requests for making predictions.
@app.route('/predict', methods=['POST'])
def predict():
     # Retrieve the data sent with the POST request and force it to be treated as JSON.
    data = request.get_json(force=True)

    # Prepare the data for prediction by creating a pandas DataFrame.
    # This DataFrame mirrors the structure expected by the trained model.
    prediction_data = pd.DataFrame({
        'Suburb': [data['suburb']],
        'Rooms': [data['rooms']],
        'Type': [data['type']],
        'Distance': [data['distance']],
        'Bathroom': [data['bathroom']],
        'Car': [data['garage']],
        'Region': [data['region']]
    })

    # Use the pre-loaded model to make a prediction based on the input data.
    prediction = model.predict(prediction_data)[0]

    # Format the prediction as a currency string.
    formatted_prediction = "${:,.2f}".format(prediction)

    # Return the prediction as a JSON response.
    return jsonify(result=formatted_prediction)

# Check if the script is executed directly and not imported.
# If it is, then start the Flask application with debugging enabled.
if __name__ == '__main__':
    app.run(debug=True) 