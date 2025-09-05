from flask import Flask

app = Flask(__name__)

CLIENT_KEY = "your_client_key_here"
REDIRECT_URI = "https://your-vercel-domain/api/callback"

@app.route("/")
def home():
    oauth_url = (
        "https://www.tiktok.com/auth/authorize?"
        f"client_key={CLIENT_KEY}&"
        "response_type=code&"
        "scope=user.info.basic,video.upload&"
        f"redirect_uri={REDIRECT_URI}&"
        "state=12345"
    )
    return f'<h1>Login with TikTok</h1><a href="{oauth_url}">Click here to login</a>'
