from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env file

app = Flask(__name__)
CORS(app)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route('/generate', methods=['POST'])
def generate_response():
    data = request.json
    prompt = data.get('prompt', '')
    mode = data.get('mode', 'chat')  # either 'chat' or 'completion'

    try:
        if mode == 'chat':
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message.content
        else:
            # For completion mode, we'll use chat completion with a different model
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7
            )
            result = response.choices[0].message.content

        return jsonify({'response': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 