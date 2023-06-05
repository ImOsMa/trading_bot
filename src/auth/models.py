from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

from src.database import Base

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer),
    Column("account_id", String, nullable=False),
    Column("token", String, nullable=False, primary_key=True),
    Column("created_date", TIMESTAMP, default=datetime.utcnow()),
)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, nullable=False,)
    account_id = Column(String, nullable=False)
    token = Column(String, nullable=False, primary_key=True)
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
