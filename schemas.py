from typing import Optional

from pydantic import BaseModel


class SAuthorizationAdd(BaseModel):
    login: str
    password: str
    mail:str
    master: Optional[bool] = None


class SAuthorization(SAuthorizationAdd):
    id: int

class SAuthorizationId(BaseModel):
    ok:bool = True
    authorization_id: int