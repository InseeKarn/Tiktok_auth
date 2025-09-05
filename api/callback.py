from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CLIENT_KEY = "sbawstaa06vtyabqgi"
CLIENT_SECRET = "fKeFdYATz6Okyuvjv0aSipGE8RNyt5Rx"
REDIRECT_URI = "https://tiktok-auth-liart.vercel.app/"

@app.route("/api/callback")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    if state != "12345":
        return "State mismatch!", 400

    # แลก code เป็น access token
    url = "https://open.tiktokapis.com/v2/oauth/token/"
    data = {
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI
    }
    response = requests.post(url, data=data).json()

    return jsonify(response)  # แสดง access token + open_id
