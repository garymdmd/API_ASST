import openai
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

#flask runclient = OpenAI(api_key=app.config['OPENAI_API_KEY'])
import os

app = Flask(__name__)

# Load your OpenAI API key from an environment variable
app.config['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY', 'default_key_for_development')
openai.api_key = app.config['OPENAI_API_KEY']


# Preloaded instructions for the assistant
assistant_instructions = """please be brief and to the point with your repsonses"""

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    
    # Combine the instructions with the user's input
    prompt = assistant_instructions + "\n\n" + user_input
    
    # Call the OpenAI API
    response = openai.completions.create(model="text-davinci-003",
    prompt=prompt,
    max_tokens=150)

    return jsonify({"response": response.choices[0].text.strip()})

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
