from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    user_input = request.json.get("message")
    
    # Initialize chat with OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_input}
        ]
    )
    
    # Extract and return the response
    if response.choices:
        ai_response = response.choices[0].message
        return jsonify({"response": ai_response})
    else:
        return jsonify({"response": "Failed to generate response!"})

if __name__ == '__main__':
    app.run()
