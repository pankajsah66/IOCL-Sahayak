from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot_logic import get_bot_response
import logging

app = Flask(__name__)
CORS(app)

# Configure Logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")
        
        if not user_message:
            return jsonify({"error": "Empty message"}), 400
            
        bot_payload = get_bot_response(user_message)
        return jsonify(bot_payload)
        
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)