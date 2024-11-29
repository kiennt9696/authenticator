from flask import jsonify

from authenticator.services import user_service


def create_user(body):
    user_service.create_user(body)
    return jsonify(), 204
