from base import AbstractUnitOfWork, Require


class Session:
    def commit(self):
        return None


def create_session_factory():
    return Session


class InternalService:
    async def find_user(self, id: int) -> dict:
        return {"name": "hello", "id": id}


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def commit(self):
        return None


class RequireUnitOfWork(Require[AbstractUnitOfWork]):
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow


class RequireInternalService(Require[InternalService]):
    def __init__(self, dependencies: InternalService):
        self.internal_service = dependencies


class RequireInternalServiceAndUnitOfWork(Require[tuple[AbstractUnitOfWork, InternalService]]):

    def __init__(self, dependencies: tuple[AbstractUnitOfWork, InternalService]):
        uow, internal_service = dependencies
        self.uow = uow
        self.internal_service = internal_service
