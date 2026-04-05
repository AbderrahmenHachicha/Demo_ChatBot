from flask import Flask , request , jsonify , render_template
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
app=Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages=[
    {"role":"system","content":"You are a helpful assistant for a CRM application called smartCRM"}

]
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/chat",methods=["POST"])
def chat():
    user_input=request.json.get("message")

    messages.append({"role":"user","content":user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages

    )
    bot_response = response.choices[0].message.content

    messages.append({"role":"assistant","content":bot_response})

    return jsonify({"response" : bot_response})


if __name__=="__main__":
    app.run(debug=True)
