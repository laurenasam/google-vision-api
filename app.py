from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

API_KEY = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual Google Cloud Vision API key
GOOGLE_VISION_API_URL = f'https://vision.googleapis.com/v1/images:annotate?key={API_KEY}'

@app.route('/analyze-image', methods=['POST'])
def analyze_image():
    image_data = request.json['imageBase64']
    
    headers = {'Content-Type': 'application/json'}
    body = {
        'requests': [{
            'image': {
                'content': image_data
            },
            'features': [{
                'type': 'LABEL_DETECTION',
                'maxResults': 10
            }]
        }]
    }

    response = requests.post(GOOGLE_VISION_API_URL, headers=headers, json=body)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

