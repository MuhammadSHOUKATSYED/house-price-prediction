from flask import Flask, request, jsonify, send_from_directory
import pickle
import numpy as np

app = Flask(__name__, static_folder='static', static_url_path='')

# Load the trained model
with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract the input data from the request
        data = request.get_json(force=True)
        
        # Extract features from the JSON data
        area = float(data['Area'])
        bedrooms = float(data['Bedrooms'])
        bathrooms = float(data['Bathrooms'])
        floors = float(data['Floors'])
        age = float(data['Age'])
        garage = 1 if data['Garage'].lower() == 'yes' else 0
        lot_size = float(data['Lot Size'])
        garden = 1 if data['Garden'].lower() == 'yes' else 0
        
        # Prepare the feature array for prediction
        features = np.array([[area, bedrooms, bathrooms, floors, age, garage, lot_size, garden]])
        
        # Make prediction
        prediction = model.predict(features)
        
        # Return the result as JSON
        return jsonify({'Predicted Price': prediction[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
