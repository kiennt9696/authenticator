from typing import Optional

from authenticator.infras.db.connection import DBConnectionHandler
from authenticator.interfaces.repositories.user_repository import IUserRepository
from authenticator.models import User


class UserRepository(IUserRepository):
    def __init__(self, db: DBConnectionHandler):
        self.session = db.session

    def create(self, user_info: dict) -> Optional[User]:
        user = User(**user_info)
        self.session.add(user)
        self.session.commit()
        return user

    def get(self, username: str) -> Optional[User]:
        user = self.session.query(User).filter_by(username=username).all()
        return user[0] if user else None
