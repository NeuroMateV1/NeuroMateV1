from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from google.cloud import aiplatform
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Retrieve environment variables
AGENT_ENGINE_RESOURCE_NAME = os.environ.get('AGENT_ENGINE_RESOURCE_NAME')
PROJECT_ID = os.environ.get('PROJECT_ID')
LOCATION = os.environ.get('LOCATION')

# Initialize Vertex AI client
if PROJECT_ID and LOCATION:
    aiplatform.init(project=PROJECT_ID, location=LOCATION)

# Route to serve the main HTML file
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Route to serve static files (CSS, JS)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/predict', methods=['POST'])
def predict():
    if not AGENT_ENGINE_RESOURCE_NAME:
        return jsonify({'error': 'AGENT_ENGINE_RESOURCE_NAME not set in environment.'}), 500

    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided.'}), 400

    try:
        # Here's where you'll call your agent. Since you have a deployed agent
        # as a reasoningEngine, we'll use the predict method.
        # This requires the google-cloud-aiplatform library.
        # The input structure depends on your agent's definition.
        # Assuming your agent expects a single string input under 'input' key.
        
        # Import the ReasoningEngine after initializing aiplatform
        from vertexai.preview.reasoning_engines import ReasoningEngine

        # Create a client for the ReasoningEngine
        agent_engine = ReasoningEngine(AGENT_ENGINE_RESOURCE_NAME)
        
        # Make the prediction request
        response = agent_engine.predict(input=user_message)
        
        # Assuming the agent returns a dictionary with an 'output' key
        agent_response_text = response.get('output', 'No output from agent.')

        return jsonify({'response': agent_response_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 