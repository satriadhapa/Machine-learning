from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('rekomendasi_model.pkl', 'rb')) #load the model

def predict_major():
    # Get request data in JSON format
    data = request.get_json()

    # Convert JSON to pandas DataFrame
    new_student = pd.DataFrame(data, index=[0])

    # Predict the major recommendation for the new student
    prediction = model.predict(new_student)

    # Return the predicted major recommendation
    return prediction[0]
if __name__ == '__main__':
    app.run(debug=True)