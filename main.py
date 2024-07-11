import webbrowser
from flask import Flask, request
from instagram_api import get_auth_url, get_access_token, get_instagram_data
import config

app = Flask(__name__)

@app.route('/')
def home():
    auth_url = get_auth_url()
    return f'<a href="{auth_url}">Login with Instagram</a>'

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = get_access_token(code)
    access_token = token_info['access_token']
    user_id = token_info['user_id']
    
    followers = get_instagram_data(user_id, access_token, 'followers')
    following = get_instagram_data(user_id, access_token, 'following')

    followers_set = set(user['username'] for user in followers)
    following_set = set(user['username'] for user in following)
    
    not_following_back = following_set - followers_set
    not_followed_back = followers_set - following_set

    return {
        "not_following_back": list(not_following_back),
        "not_followed_back": list(not_followed_back)
    }

if __name__ == '__main__':
    app.run(debug=True)
