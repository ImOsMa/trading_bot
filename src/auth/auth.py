from sqlalchemy import select, insert
from sqlalchemy.orm import Session, sessionmaker
from src.database import get_session
from src.auth.models import user
from src.auth.schemas import AccountAdd


class Auth:

    @staticmethod
    def add_new_account_for_user(new_account: AccountAdd, session: Session = get_session()):
        stmt = insert(user).values(**new_account.dict())
        session.execute(stmt)
        session.commit()
        return {"status": "success"}

    @staticmethod
    def get_user_by_id(user_id: int, session: Session = get_session()):
        query = select(user).where(user.c.id == user_id)
        result = session.execute(query)
        return result.all()

    @staticmethod
    def get_user_by_account_id(account_id: str, session: Session = get_session()):
        query = select(user).where(user.c.account_id == account_id)
        result = session.execute(query)
        return result.all()

    @staticmethod
    def get_user_by_token(token: str, session: Session = get_session()):
        query = select(user).where(user.c.token == token)
        result = session.execute(query)
        return result.all()


