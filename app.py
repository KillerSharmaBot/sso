import requests
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return Response(requests.get("https://raw.githubusercontent.com/KillerSharmaBot/sso/main/index.html").text, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)