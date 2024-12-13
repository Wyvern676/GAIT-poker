from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Is this thing on?"

app.run(host="0.0.0.0", port=5000)

