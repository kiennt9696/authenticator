from flask import jsonify

from authenticator.services import authentication_service


def login(body=None):
    username = body.get("username")
    password = body.get("password")
    session_token = authentication_service.login(username, password)
    res = {
        "message": "Login successfully",
        "session_token": session_token,
    }
    return jsonify(res), 200
