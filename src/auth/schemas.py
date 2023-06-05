from datetime import datetime

from pydantic import BaseModel


class AccountAdd(BaseModel):
    id: int
    account_id: str
    token: str
