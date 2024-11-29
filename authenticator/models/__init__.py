from uuid import uuid4

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, DateTime, create_engine
from datetime import datetime

Base = declarative_base()


def _uuid4():
    return str(uuid4())


class AuditTable(Base):
    __abstract__ = True
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
    updated_by = Column(String, nullable=True)


class User(AuditTable):
    __tablename__ = "user"
    id = Column(String, primary_key=True, default=_uuid4)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    active = Column(Boolean, default=True)


if __name__ == "__main__":
    db_uri = "postgresql+psycopg2://postgres:postgres@127.0.0.1:8432/access?application_name=authenticator"
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
