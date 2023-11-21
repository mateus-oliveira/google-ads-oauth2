from flask import Flask, redirect, session, request
from auth.auth import authentication, oauth2callback

_CLIENT_URL = 'http://localhost:4200'

app = Flask(__name__)
app.secret_key = "SECRET KEY"

@app.route('/authentication')
def authentication_endpoint():
    auth_info = authentication()
    passthrough_val = auth_info['passthrough_val']
    session['passthrough_val'] = passthrough_val
    url = auth_info['authorization_url']
    return redirect(url)


@app.route('/oauth2callback')
def oauth2callback_endpoint():
    passthrough_val = session['passthrough_val']
    state = request.args.get("state")
    code = request.args.get("code")
    oauth2callback(passthrough_val, state, code)

    return redirect(_CLIENT_URL)
