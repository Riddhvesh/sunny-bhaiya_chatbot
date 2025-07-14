from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Pre-defined funny replies based on personality
replies = {
    "sunny": [
        "Abe oye! Kya bakchodi kar raha hai?",
        "Mummy kasam, tu toh full tension de raha hai!",
        "Aree chill bhai, chai peete hain!"
    ],
    "delhi_bhai": [
        "Bhai tu toh scene mein hi heavy hai!",
        "Dilli se hoon, attitude laazmi hai!",
        "Bhai, pehle gym phir gyaan!"
    ],
    "cricket_fan": [
        "Kohli form mein hai toh India jeetega!",
        "Koi garden mai ghumega ...?!",
        "Har match final jaisa lagta hai yaar!"
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.json.get("msg")
    personality = request.json.get("personality")
    reply = random.choice(replies.get(personality, ["Arey main kya bolu bhai, samajh nahi aaya!"]))
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
