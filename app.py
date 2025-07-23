from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env file

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route('/generate', methods=['POST'])
def generate_response():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'response': 'No prompt provided'}), 400
    prompt = data['prompt']
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        result = response.choices[0].message.content
        return jsonify({'response': result})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 