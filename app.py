from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np

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
        'Type': [data['type']],
        'Rooms': [data['rooms']],
        'Bathroom': [data['bathroom']],
        'Distance': [data['distance']],
        'Car': [data['garage']],
        'Suburb': [data['suburb']],
        'Region': [data['region']]
    })

    # Convert the DataFrame to a NumPy array to remove feature names
    prediction_data_np = prediction_data.to_numpy()

    # Use the pre-loaded model to make a prediction based on the input data.
    log_price_predictions = model.predict(prediction_data_np)[0]

    # Convert the log price predictions back to actual prices
    prediction = np.exp(log_price_predictions)

    # Format the prediction as a currency string.
    formatted_prediction = "${:,.2f}".format(prediction)

    # Return the prediction as a JSON response.
    return jsonify(result=formatted_prediction)

# Check if the script is executed directly and not imported.
# If it is, then start the Flask application with debugging enabled.
if __name__ == '__main__':
    app.run(debug=True) 