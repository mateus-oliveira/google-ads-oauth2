import os
import hashlib

from google_auth_oauthlib.flow import Flow


_CLIENT_SECRETS_PATH = os.environ['CLIENT_SECRETS_PATH']
_SCOPE = "https://www.googleapis.com/auth/adwords"
_SERVER = "127.0.0.1"
_PORT = 5000
_REDIRECT_URI = f"http://{_SERVER}:{_PORT}/oauth2callback"


def authentication():
    flow = Flow.from_client_secrets_file(_CLIENT_SECRETS_PATH, scopes=[_SCOPE])
    flow.redirect_uri = _REDIRECT_URI

    passthrough_val = hashlib.sha256(os.urandom(1024)).hexdigest()

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        state=passthrough_val,
        prompt="consent",
        include_granted_scopes="true"
    )

    print(f'authorization url: {authorization_url}')

    return {
        "authorization_url": authorization_url,
        "passthrough_val": passthrough_val,
    }


def oauth2callback(passthrough_val, state, code):
    if passthrough_val != state:
        message = "State token does not match the expected state."
        raise ValueError(message)
    
    flow = Flow.from_client_secrets_file(_CLIENT_SECRETS_PATH, scopes=[_SCOPE])
    flow.redirect_uri = _REDIRECT_URI
    flow.fetch_token(code=code)
    refresh_token = flow.credentials.refresh_token
    print(f"\nYour refresh token is: {refresh_token}\n")
