from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pickle

# Load the model
model = pickle.load(open('sentiment_analysis_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    text = data['text']

    # sentiment analysis
    prediction = model.predict([text])
    response = {
        'text': text,
        'sentiment': prediction[0]
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)