from common_utils.exception import InvalidParameter
from werkzeug.security import generate_password_hash

from authenticator.interfaces.repositories.user_repository import IUserRepository
from helpers.validation import is_email_valid, is_password_strong


class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def create_user(self, user_info: dict):
        username = user_info.get("username")
        password = user_info.get("password")
        email = user_info.get("email")
        phone = user_info.get("phone")
        firstname = user_info.get("firstname")
        lastname = user_info.get("lastname")
        if not is_email_valid(email):
            raise InvalidParameter(
                error_code=4001003, params="email", message="email is invalid"
            )
        if not is_password_strong(password):
            raise InvalidParameter(
                error_code=4001004,
                params="password",
                message="password is not strong enough",
            )

        user = {
            "username": username,
            "password_hash": generate_password_hash(password),
            "email": email,
            "phone": phone,
            "firstname": firstname,
            "lastname": lastname,
        }
        self.user_repo.create(user)
