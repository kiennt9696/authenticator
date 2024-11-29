from authenticator.repositories import user_repo
from authenticator.services.authentication import AuthenticationService
from authenticator.services.user import UserService

authentication_service = AuthenticationService(user_repo=user_repo)
user_service = UserService(user_repo=user_repo)
