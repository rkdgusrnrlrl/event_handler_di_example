import pytest

from events import UserCreated
from factories import factory_handler


@pytest.mark.asyncio
async def test_factory():
    event = UserCreated(user_id=1)
    handler = factory_handler(event)
    await handler.handler(event)
