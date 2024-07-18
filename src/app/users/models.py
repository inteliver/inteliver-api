from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.postgres import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    name = Column(String, nullable=False)
    email_username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    cloud_name = Column(String, nullable=False)
    endpoint = Column(String, nullable=False)
    storage_limit = Column(Integer, nullable=False)
    transaction_limit = Column(Integer, nullable=False)
    role = Column(String, nullable=False, default="user")
