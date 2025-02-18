from flask import Flask, request, jsonify
import pickle
import pandas as pd
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Load the pre-trained model (Gradient Boosting is available)
with open('gb_model', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Convert input to DataFrame; 
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)
    app.logger.info(f"Incoming request with data: {data}, Prediction: {prediction[0]}")
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
