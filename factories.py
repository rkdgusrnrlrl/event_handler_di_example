from typing import Type

from events import Event, UserCreated
from handlers import AbstractHandler, SyncUserDateHandler
from infrastructure.base import RequireInternalService, InternalService

event_mapper_handler: dict[Type[Event], Type[AbstractHandler]] = {
    UserCreated: SyncUserDateHandler
}


def factory_handler(event: Event) -> AbstractHandler:
    handler_cls = event_mapper_handler[event.__class__]
    handler = handler_cls()
    if isinstance(handler, RequireInternalService):
        handler_cls(dependencies=InternalService())
    return handler
