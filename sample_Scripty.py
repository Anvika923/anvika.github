import requests
from requests.auth import HTTPBasicAuth
import json



def get_access_token(oauth_settings):
    """
    Get OAuth access token using client_id, client_secret, and refresh_token.
    """
    url = "https://services1.myworkday.com/ccx/oauth2/okgov/token"
    client_id= "MGMxZDBmZmEtYzZhNS00MWU5LWI4YTMtODIwMWRmZGFkY2Fj"
    client_secret="n21jjkl59a7mlgdippdtf27n06d2gsalz3x1wblp26k9qptf6do5fx7ilzfzk6y1z9gf55873h8e5c1h3irp1ywu8r79mq8z4vs"
    refresh_token="12i9dzupm3zfntx9qj7yv1uf7f5yaw8ij5z1penxein8axftupx100two40epn7c9s3u522jcuyqv94w8sbyemouescgzpznawlc"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "refresh_token",
        "refresh_token": oauth_settings["refresh_token"]
    }

    response = requests.post(
        url,
        headers=headers,
        data=data,
        auth=HTTPBasicAuth(oauth_settings["client_id"], oauth_settings["client_secret"])
    )

    if response.status_code == 200:
        token = response.json().get("access_token")
        print("[INFO] Access token generated successfully.")
        return token
        print(token)
    else:
        raise Exception(f"[ERROR] Token generation failed: {response.status_code} {response.text}")
        

