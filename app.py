import openai
from flask_cors import CORS
from flask import *
from dotenv import load_dotenv 
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app) 

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    task_description = request.get_json().get('task_description')
    programming_language = request.get_json().get('programming_language')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a knowledgeable programming assistant."},
            {"role": "user", "content": f"Generate a piece of code in {programming_language} that accomplishes the following task: {task_description}. The code should include any specific requirements or constraints, handle edge cases, optimize for performance, include comments, and follow best practices."}
        ],
        max_tokens=2048,
        temperature=0.7,
    )
    generated_code = response.choices[0]['message']['content'].strip()
    return jsonify({'generated_code': generated_code})

if __name__ == '__main__':
    app.run(debug=True)
