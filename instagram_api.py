import requests
from urllib.parse import urlencode
import config

def get_auth_url():
    params = {
        'client_id': config.CLIENT_ID,
        'redirect_uri': config.REDIRECT_URI,
        'scope': 'user_profile,user_media',
        'response_type': 'code'
    }
    auth_url = f"https://api.instagram.com/oauth/authorize?{urlencode(params)}"
    return auth_url

def get_access_token(auth_code):
    token_url = 'https://api.instagram.com/oauth/access_token'
    data = {
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'redirect_uri': config.REDIRECT_URI,
        'code': auth_code
    }
    response = requests.post(token_url, data=data)
    return response.json()

def get_instagram_data(user_id, access_token, relationship):
    url = f"https://graph.instagram.com/{user_id}/{relationship}?fields=username&access_token={access_token}"
    response = requests.get(url)
    return response.json().get('data', [])
