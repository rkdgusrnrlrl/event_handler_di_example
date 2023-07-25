from typing import Type

from events import Event, UserCreated
from handlers import AbstractHandler, SyncUserDateHandler
from infrastructure.base import RequireInternalService, InternalService, UnitOfWork, RequireUnitOfWork

event_mapper_handler: dict[Type[Event], Type[AbstractHandler]] = {
    UserCreated: SyncUserDateHandler
}


class HandlerFactory:
    def __init__(self, uow_cls: Type[UnitOfWork], session_factory, internal_service: InternalService):
        self.uow_cls = uow_cls
        self.session_factory = session_factory
        self.internal_service = internal_service

    def create_handler(self, event: Event) -> AbstractHandler:
        handler_cls = event_mapper_handler[event.__class__]

        if issubclass(handler_cls, RequireInternalService):
            return handler_cls(dependencies=self.internal_service)  # type:ignore
        elif issubclass(handler_cls, RequireUnitOfWork):
            return handler_cls(dependencies=self.uow_cls(session_factory=self.session_factory))  # type:ignore
        return handler_cls()
