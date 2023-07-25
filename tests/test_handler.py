import pytest

from events import UserCreated
from factories import HandlerFactory
from infrastructure.base import Session, UnitOfWork, InternalService


class FakeSession(Session):
    ...


class FakeInternalService(InternalService):
    ...


@pytest.mark.asyncio
async def test_factory():
    event = UserCreated(user_id=1)

    handler_factory = HandlerFactory(
        session_factory=FakeSession,
        uow_cls=UnitOfWork,
        internal_service=FakeInternalService()
    )
    handler = handler_factory.create_handler(event)
    await handler(event)
