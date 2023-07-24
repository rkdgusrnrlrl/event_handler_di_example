from base import AbstractUnitOfWork, Require


class InternalService:
    async def find_user(self, id: int) -> dict:
        return {"name": "hello", "id": id}


class UOW(AbstractUnitOfWork):
    async def commit(self):
        return None


class RequireUnitOfWork:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow


class RequireInternalService(Require[InternalService]):
    internal_service: InternalService | None = None

    def set_dependency_inject(self, dependencies: InternalService):
        self.internal_service = dependencies


class RequireInternalServiceAndUnitOfWork(Require[tuple[AbstractUnitOfWork, InternalService]]):
    uow: AbstractUnitOfWork | None = None
    internal_service: InternalService | None = None

    def set_dependency_inject(self, dependencies: tuple[AbstractUnitOfWork, InternalService]):
        uow, internal_service = dependencies
        self.uow = uow
        self.internal_service = internal_service
