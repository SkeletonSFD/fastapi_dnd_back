from typing import Optional
from  sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    "sqlite+aiosqlite:///authorization.db"
)
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass
class AuthorizationOrm(Model):
    __tablename__ = "authorization"

    id:Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
    mail: Mapped[str]
    master: Mapped[Optional[str]]

async def create_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.drop_all)