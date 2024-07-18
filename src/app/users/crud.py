from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.users.models import User
from app.users.schemas import UserCreate, UserUpdate
from app.auth.hash import get_password_hash, verify_password
import uuid


async def get_user(db: AsyncSession, user_id: uuid.UUID):
    return await db.get(User, user_id)


async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email_username == email))
    return result.scalars().first()


async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(
        name=user.name,
        email_username=user.email_username,
        password=get_password_hash(user.password),
        cloud_name=user.cloud_name,
        endpoint=user.endpoint,
        storage_limit=user.storage_limit,
        transaction_limit=user.transaction_limit,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def update_user(db: AsyncSession, user_id: uuid.UUID, user_update: UserUpdate):
    db_user = await get_user(db, user_id)
    if db_user:
        for key, value in user_update.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        await db.commit()
        await db.refresh(db_user)
        return db_user
    return None


async def delete_user(db: AsyncSession, user_id: uuid.UUID):
    db_user = await get_user(db, user_id)
    if db_user:
        await db.delete(db_user)
        await db.commit()
        return db_user
    return None


async def authenticate_user(db: AsyncSession, email: str, password: str):
    user = await get_user_by_email(db, email)
    if user and verify_password(password, user.password):
        return user
    return None
