from authenticator.extension import db
from authenticator.repositories.user import UserRepository


user_repo = UserRepository(db=db)
