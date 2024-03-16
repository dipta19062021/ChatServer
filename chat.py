import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
    
genai.configure(api_key='AIzaSyDYn7gq1jAJyk_gUq1G6ZimnkZO8usJmLw')

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response
#In=input("Enter the text")
#out= print(get_gemini_response(In))

    
@app.route("/chatbot/", methods=["POST"])
def chatbot():
    data = request.json
    text = data["text"]
    for chunk in get_gemini_response(text):
        response= chunk.text
        return jsonify({"response": response})
    
if __name__ == "__main__":
    app.run(debug=True)