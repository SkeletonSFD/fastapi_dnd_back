from sqlalchemy import select
from database import new_session, AuthorizationOrm
from schemas import SAuthorizationAdd, SAuthorization


class AuthorizationRepisitory:
    @classmethod
    async def add_one(cls, data: SAuthorizationAdd) -> int:
        async with new_session() as session:
            authorization_dict = data.model_dump()
            task = AuthorizationOrm(**authorization_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) ->list[SAuthorization]:
        async with new_session() as session:
            query = select(AuthorizationOrm)
            result = await session.execute(query)
            authorization_models = result.scalars().all()
            authorization_schemas = [SAuthorization.model_validate(authorization_model) for authorization_model in authorization_models]
            return authorization_schemas