import os

from dotenv import load_dotenv
from sqlalchemy import ForeignKey, String, BigInteger, Date, DateTime, func
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.schema import CreateSchema


load_dotenv()

DB_USER: str | None = os.getenv("DB_USER")
DB_PASSWORD: str | None = os.getenv("DB_PASSWORD")
DB_HOST: str | None = os.getenv("DB_HOST")
DB_PORT: str | None = os.getenv("DB_PORT")
DB_DATABASE: str | None = os.getenv("DB_DATABASE")

DATABASE_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
SCHEMA_NAME: str = "bot_any"

engine = create_async_engine(url=DATABASE_URL, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': SCHEMA_NAME}

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger, nullable=False)
    tg_name = mapped_column(String(255))
    user_full_name = mapped_column(String(255), nullable=True)
    register_dt = mapped_column(Date, default=func.now(), nullable=False)

    def __str__(self):
        return f"id: {self.id}, tg_id: {self.tg_id}, tg_name:{self.tg_name}, user_full_name: {self.user_full_name}, register_dt:{self.register_dt}"

# class Orders(Base):
#     __tablename__ = 'Items'
#     __table_args__ = {'schema': SCHEMA_NAME}
#
#     id:
#     user_id =


async def async_main():
    async with engine.begin() as conn:
        await conn.execute(CreateSchema(SCHEMA_NAME, if_not_exists=True))
        await conn.run_sync(Base.metadata.create_all)


#df = pd.read_excel(Items.xlsx, sheet_name='Товары')
#df.to_sql('Items',connection,if_exists='replace')