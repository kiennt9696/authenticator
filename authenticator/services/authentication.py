import datetime

from common_utils.exception import InvalidParameter
from common_utils.token import encode_jwt
from flask import current_app
from werkzeug.security import check_password_hash

from authenticator.interfaces.repositories.user_repository import IUserRepository


class AuthenticationService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def __generate_session_token(self, username: str, user_id: str):
        jwt_message = {
            "iss": "authenticator",
            "username": username,
            "sub": user_id,
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(
                seconds=current_app.config.get("TOKEN_EXPIRATION_TIME", 3600)
            ),
        }
        return encode_jwt(jwt_message, current_app.config.get("PRIVATE_KEY"))

    def login(self, username: str, password: str) -> str:
        user_info = self.user_repo.get(username=username)
        if not user_info:
            raise InvalidParameter(
                error_code=4001002,
                params="username or password",
                message="username or password is incorrect",
            )
        if not check_password_hash(user_info.password_hash, password):
            raise InvalidParameter(
                error_code=4001002,
                params="username or password",
                message="username or password is incorrect",
            )
        return self.__generate_session_token(username, user_info.id)
