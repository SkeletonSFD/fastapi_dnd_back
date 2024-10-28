from typing import Annotated
from fastapi import APIRouter, Depends
from repository import AuthorizationRepisitory
from schemas import SAuthorizationAdd, SAuthorization, SAuthorizationId

router = APIRouter(
    prefix="/authorization",
    tags=["authorization"],
)


@router.post("")
async def add_task(
        task: Annotated[SAuthorizationAdd, Depends()],
)-> SAuthorizationId:
    authorization_id = await AuthorizationRepisitory.add_one(task)
    return {"ok": True, "authorization_id": authorization_id}

@router.get("")
async def get_tasks()->list[SAuthorization]:
    authorizations = await AuthorizationRepisitory.find_all()
    return {"authorizations": authorizations}